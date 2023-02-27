from api import create_app
from api.config.config import config_dict

app = create_app(config=config_dict['prod'])    # to run on heroku for the production stage
# app = create_app()      # to run locally for the testing process

if __name__=="__main__":
    app.run()