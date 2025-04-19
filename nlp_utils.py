def interpret_command(command):
    command = command.lower()

    if "weather" in command:
        city = command.split("in")[-1].strip() if "in" in command else "Delhi"
        return {"intent": "weather", "city": city}

    elif "play music" in command or "song" in command:
        return {"intent": "music"}

    elif "exit" in command or "bye" in command:
        return {"intent": "exit"}

    else:
        return {"intent": "query", "query": command}
