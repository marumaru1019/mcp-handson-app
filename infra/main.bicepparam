using './main.bicep'

param environmentName = readEnvironmentVariable('AZURE_ENV_NAME', '')
param location = readEnvironmentVariable('AZURE_LOCATION', 'japaneast')
param apiImageName = readEnvironmentVariable('SERVICE_API_IMAGE_NAME', '')
