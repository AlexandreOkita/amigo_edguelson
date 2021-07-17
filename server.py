from configureEvents import configureEvents
from di.GlobalObjects import discordService

if __name__ == "__main__":
    configureEvents(discordService.client)
    discordService.runServer()