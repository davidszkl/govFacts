echo "cat /workspaces/.devcontainer/swag" >> ~/.bashrc

echo "echo dbgate: http://localhost:3030" >> ~/.bashrc

make -C /workspaces/app/ init

echo "Hello World! ~UwU~"