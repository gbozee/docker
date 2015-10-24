export PYTHONPATH=${BASE_DIR}:${BASE_DIR}/src
# Add site-packages to PYTHONPATH ??
for l in $(rpm -ql python-libs | grep site-packages |grep -vi readme)
do
    export PYTHONPATH=${PYTHONPATH}:${l}
done
