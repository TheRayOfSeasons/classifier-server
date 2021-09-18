#!/usr/bin/env bash

# --------------------------------------------
#
# *GENERATE KEYS*
# 
# This bash script fetches all secrets defined
# in parameter store based on the environment
# defined in CodeBuild.
#
# --------------------------------------------

export APP_NAME="classifier"

# NOTE: Define the environment in CodeBuild beforehand to use prod.
if [ "${environment}" == "production" ] ||  [ "${environment}" == "prod" ]
then
  echo "Using production secrets..."
  export ENVIRONMENT=prod
elif [ "${environment}" == "staging" ]
  echo "Using staging secrets..."
  export ENVIRONMENT=staging
else
  echo "Using custom secrets..."
  export ENVIRONMENT=${environment}
fi

echo "Environment: ${ENVIRONMENT}"

function get_keys_from_ssm
{
  echo "\"$(aws ssm get-parameter --name /${APP_NAME}/${ENVIRONMENT}/${$1}--query Parameter.Value)\""
}

export MIGRATION_MANAGER_KEYS="
{
  DEBUG: false,
  SECRET_KEY: $(get_keys_from_ssm SECRET_KEY),
  DATABASE_ENGINE: $(get_keys_from_ssm DATABASE_ENGINE),
  DATABASE_NAME: $(get_keys_from_ssm DATABASE_NAME),
  DATABASE_HOST: $(get_keys_from_ssm DATABASE_HOST),
  DATABASE_PORT: $(get_keys_from_ssm DATABASE_PORT),
  DATABASE_USER: $(get_keys_from_ssm DATABASE_USER),
  DATABASE_PASSWORD: $(get_keys_from_ssm DATABASE_PASSWORD),
}
"

echo "$(python build_scripts/format_keys.py)" > migration_manager/keys.json
