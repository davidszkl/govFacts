from state.State import State

state = None
app = None

if __name__ == "main":
    state = State()
    app = state.app

    from datasources import *
    state.loadDataSources()
