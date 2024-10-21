import os
import shutil
from loguru import logger
from .config import config
from .logging_setup import LoggerSetup
from .converter import JSON2TOML

def main():
    LoggerSetup.setup_logger(config.get('Logging', 'log_filepath', fallback='logs'), 
                             config.get('Logging', 'log_filename', fallback='app'))
    logger.info(f"Application Started. Debug mode: {'ON' if config.debug_mode else 'OFF'}")
    
    json_file = config.get('Files', 'json_file', fallback=input("Enter JSON file path: "))
    toml_file = config.get('Files', 'toml_file', fallback="output.toml")
    output_folder = "output"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logger.info(f"Created Output folder: {output_folder}")
    else:
        logger.info(f"Output folder already exists: {output_folder}")
    
    json2toml = JSON2TOML(json_file, toml_file)
    success, elapsed_time = json2toml.convert_json2toml()
    
    if success:
        logger.info("Successfully Converted JSON to TOML")
        if os.path.exists(toml_file):
            download_toml = f"{os.path.basename(os.path.splitext(json_file)[0])}.toml"
            output_filepath = os.path.join(output_folder, download_toml)
            try:
                shutil.copy(toml_file, output_filepath)
                logger.info(f"Converted TOML file copied to: {output_filepath}")
            except Exception as e:
                logger.error(f"Error copying file: {e}")
        else:
            logger.error(f"Error: TOML file {toml_file} not found.")
        logger.info(f"Time taken for conversion: {elapsed_time:.3f} seconds")
    else:
        logger.error("Failed to convert JSON to TOML")
    
    logger.info("Application Finished.")

if __name__ == '__main__':
    main()
