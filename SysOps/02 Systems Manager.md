# Custom Run Database Command

```json
{
    "schemaVersion": "2.2",
    "description": "Runs a postgresql script and applies it to the database.",
    "parameters": {
      "sqlFile": {
        "type": "String",
        "default": "",
        "description": "(Required) The SQL file name stored in s3.",
        "maxChars": 4096
      },
      "databaseHost": {
        "type": "String",
        "default": "",
        "description": "(Required) The database DNS host name",
        "maxChars": 4096
      },
      "databasePort": {
        "type": "String",
        "default": "5432",
        "description": "(Required) The database port",
        "maxChars": 4096
      },
      "dbName": {
        "type": "String",
        "description": "(Required) The database name the SQL file will execute in",
        "maxChars": 4096
      },
      "dbUsername": {
        "type": "String",
        "description": "(Required) The username this command will use.",
        "maxChars": 4096
      },
      "dbPassword": {
        "type": "String",
        "description": "(Required) The database password stored in a parameter store secure string.",
        "maxChars": 4096
      },
      "workingDirectory": {
        "type": "String",
        "default": "",
        "description": "(Optional) The path to the working git directory on your instance.",
        "maxChars": 4096
      },
      "executionTimeout": {
        "type": "String",
        "default": "3600",
        "description": "(Optional) The time in seconds for a command to complete before it is considered to have failed. Default is 3600 (1 hour). Maximum is 172800 (48 hours).",
        "allowedPattern": "([1-9][0-9]{0,4})|(1[0-6][0-9]{4})|(17[0-1][0-9]{3})|(172[0-7][0-9]{2})|(172800)"
      }
    },
    "mainSteps": [
      {
        "action": "aws:runShellScript",
        "name": "RunSQL",
        "inputs": {
          "workingDirectory": "{{ workingDirectory }}",
          "timeoutSeconds": "{{ executionTimeout }}",
          "runCommand": [
            "#!/bin/bash",
            "aws s3 cp {{sqlFile}} /tmp/file.sql",
            "export PGPASSWORD=`aws --region=ap-southeast-1 ssm get-parameter --name {{dbPassword}} --with-decryption --output text --query Parameter.Value`",
            "psql -h {{databaseHost}} -p {{databasePort}} -d {{dbName}} -U {{dbUsername}} -f /tmp/file.sql"
          ]
        }
      }
    ]
  }
```

