from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
print("Project found at: ", BASE_PATH)
path_to_model_data = Path.joinpath(BASE_PATH, "model_data")
