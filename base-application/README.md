Application tree-map for the reference

    base-application
    ├───app
    │   ├───assets          # assets directory contain static files like image, css, etc.
    │   │   └───img
    │   ├───config          # config directory can be used to do configuration like DB configuration or other environment related
    │   ├───src
    │   │   ├───blueprints  # Blueprint play the role of controller all the request land to the blueprints first then will be redirected to the other service
    │   │   │   └───__pycache__
    │   │   ├───database    # All the DB related files should be stored in database directory
    │   │   ├───exceptions  # Central point to handle all the exceptions
    │   │   ├───services    # Developer should write all the logical functionals inside the services directory
    │   │   └───__pycache__
    │   └───__pycache__
    └───app_test            # app_test directory is responsible to handle all the test cases units and functional
        ├───assets
        │   └───img
        ├───functionals     # Write all the funtional test-cases inside this directory
        ├───units           # Write all the unit test-cases inside this directory
        └───Dockerfile      # Docker configuration file