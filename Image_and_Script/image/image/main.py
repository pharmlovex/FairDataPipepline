import os
import platform
import process_image from imgAnalysis

sys.path.append(str(os.getcwd()))
import data_pipeline_api as pipeline  # noqa: E402

token = str(os.environ.get("FDP_LOCAL_TOKEN"))
script = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "script.sh")
if platform.system() == "Windows":
    script = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "script.bat")
config = os.path.join(str(os.environ.get("FDP_CONFIG_DIR")), "config.yaml")
handle = pipeline.initialise(token, config, script)

image_file = pipeline.link_read(handle, "work/FairDataPipepline/Image_and_Script/image/image/single_frame_image.tif")
image_prop = pipeline.link_write(
    handle, "image/results/image_analysis"
)
image_mask = pipeline.link_write(handle, "image/results/image_mask")

process_image(image_file, image_prop, image_mask)


pipeline.finalise(token, handle)

