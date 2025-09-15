# databricks-assetbundle-101
- https://github.com/databricks/bundle-examples/tree/main/knowledge_base/databricks_app
- https://docs.databricks.com/aws/en/dev-tools/bundles/settings
- To reset databricks asset bundle state simply delete __.databricks__ folder, and after we run __databricks bundle deploy__ it will recreate the __.databricks__ folder with updated state information

#### Runtime
- we need to find LTS[long time support] version
- 15.4 LTS, Spark - 3.5.0, Python - 3.11

#### virtual enev
    ```sh
    python3.11 -m venv .venv
    source .venv/bin/activate
    pip list
    pip install pandas==2.2 
    pip freeze > requirements.txt
    pip install -r requirements.txt
    deactivate
    ```

#### databricks cli installation
- Installation - https://docs.databricks.com/aws/en/dev-tools/cli/install 
- CLI Commands - https://learn.microsoft.com/en-us/azure/databricks/dev-tools/cli/commands
- Verify Installation
    ```sh
    which -a databricks # find all versions
    /usr/local/bin/databricks -v # select one
    export PATH="/usr/local/bin:$PATH" # set this version
    databricks -v / --version
    databricks -h / --help
    ```
- Authenticate
    ```sh
    databricks configure -h
    databricks configure --host https://dbc-26546341-69b4.cloud.databricks.com/ --profile databricks-playground
    databricks auth profiles
    databricks auth describe --profile databricks-playground
    ```
- To Modify profiles
    ```sh
    nano ~/.databrickscfg # edit config file
    databricks auth profiles # show profiles
    ```
- CLI 
    - Create Cluster
    ```sh
    databricks clusters create --json @create-compute.json --profile personal-dev
    databricks clusters list --profile personal-dev # list all clusters
    databricks clusters delete 0912-112925-huehhz3d --profile personal-dev # show on UI as terminated cluster
    databricks clusters permanent-delete 0728-154234-7gcut6ku --profile eurostar-dev # delete from UI
    ```

#### databricks bundle
- cli 
    ```sh
    databricks bundle -h
    databricks bundle init --profile databricks-playground # enter bundle name lets say dab_project
    cd dab_project
    databricks bundle summary --profile databricks-playground # show location where bundle will be deployed
    databricks bundle validate --profile databricks-playground # setup bundle .toml file
    databricks bundle deploy --profile databricks-playground # deploy the bundle
    databricks bundle deploy --target stg --profile databricks-playground # deploy to specific enev, based on databricks.yml
    databricks bundle deploy --target prod --profile databricks-playground
    databricks bundle destroy --target prod --profile databricks-playground # delete all resources, jobs, etc..
    ```

#### databricks connect
- https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect/python/advanced
    ```sh
    python -m pip install databricks-connect==15.1.* --disable-pip-version-check --no-python-version-warning
    ```
