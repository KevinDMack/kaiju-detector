import os
import sys
import json
import glob
import gdal
import logging

from pathlib import Path

def convert_directory(
    input_path,
    output_path,
    config_file,
    logger,
    default_options={"format": "png", "metadata": False},
):
    logger.info("looking for config file: %s", config_file)

    translate_options_dict = default_options
    logger.debug("default config options: %s", translate_options_dict)

    try:
        with open(config_file, "r") as config:
            config_file_dict = json.load(config)
            logger.debug("read in %s", config_file_dict)
            translate_options_dict.update(config_file_dict)
    except Exception as e:
        logger.error("error reading config file %s", e)
        sys.exit(1)

    logger.info("using config options: %s", translate_options_dict)

    keep_metadata = translate_options_dict.pop("metadata")

    opt = gdal.TranslateOptions(**translate_options_dict)

    logger.debug("looking for input files in %s", input_path)
    for in_file in os.scandir(input_path):
        in_name = in_file.name
        logger.info("ingesting file %s", in_file.path)
        # ! this is a landmine; will error for files w/o extension but with '.', and for formats with spaces
        out_name = os.path.splitext(in_name)[0] + "." + translate_options_dict["format"]
        out_path = os.path.join(output_path, out_name)
        try:
            gdal.Translate(out_path, in_file.path, options=opt)
        except Exception as e:
            logger.error("gdal error: %s", e)
            sys.exit(1)
        else:
            logger.info("successfully translated %s", out_path)

    if not keep_metadata:
        xml_glob = os.path.join(output_path, "*.aux.xml")
        logger.debug(f"deleting metadata files that match {xml_glob}")
        for xml_file in glob.glob(xml_glob):
            logger.debug(f"deleting metadata file f{xml_file}")
            os.remove(xml_file)


if __name__ == "__main__":
    input_path = os.path.abspath(os.environ["APP_INPUT_DIR"])
    output_path = os.path.abspath(os.environ["APP_OUTPUT_DIR"])
    config_file = os.path.abspath(os.environ["APP_CONFIG"])

    Path(output_path).mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    )
    logger = logging.getLogger("image_convert")

    convert_directory(input_path, output_path, config_file, logger)
