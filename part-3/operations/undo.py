import state


# pop the last img array from our state and display the second last
def last():
	if len(state.history) > 1:
		state.history.pop()
		state.logs.append("undo")
	else:
		print("Nothing to undo.")
	return state.history[-1].copy()
