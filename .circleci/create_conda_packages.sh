# Install conda dependencies
conda install -y conda-build conda-verify zip

# Perform build
conda build --python $PYTHON_VERSION recipe/

# Convert to other architectures
mkdir -p ./conda_packages_${PYTHON_VERSION}/linux-64/
cp /opt/conda/conda-bld/linux-64/plotly-*.tar.bz2 ./conda_packages_${PYTHON_VERSION}/linux-64/
conda convert -p linux-32 ./conda_packages_${PYTHON_VERSION}/linux-64/plotly-*.tar.bz2 -o ./conda_packages_${PYTHON_VERSION}/
conda convert -p osx-64 ./conda_packages_${PYTHON_VERSION}/linux-64/plotly-*.tar.bz2 -o ./conda_packages_${PYTHON_VERSION}/
conda convert -p win-64 ./conda_packages_${PYTHON_VERSION}/linux-64/plotly-*.tar.bz2 -o ./conda_packages_${PYTHON_VERSION}/
conda convert -p win-32 ./conda_packages_${PYTHON_VERSION}/linux-64/plotly-*.tar.bz2 -o ./conda_packages_${PYTHON_VERSION}/

# zip up packages into artifacts directory
mkdir artifacts
zip -r artifacts/conda_packages_${PYTHON_VERSION}.zip ./conda_packages_${PYTHON_VERSION}/