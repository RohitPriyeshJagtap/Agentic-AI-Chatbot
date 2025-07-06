from configparser import ConfigParser

class Config:
    def __init__(self, config_file="src/langgraphagenticai/ui/uiconfigfile.ini"):
        from os.path import abspath, exists
        abs_path = abspath(config_file)
        print(f"[DEBUG] Loading config from: {abs_path}")
        self.config = ConfigParser()
        read_files = self.config.read(config_file)
        print(f"[DEBUG] Config files read: {read_files}")
        print(f"[DEBUG] Sections: {self.config.sections()}")
        print(f"[DEBUG] DEFAULT keys: {list(self.config['DEFAULT'].keys())}")

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")