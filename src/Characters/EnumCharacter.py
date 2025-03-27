from enum import Enum
from src.Characters.TownsFolk.C_WasherWoman import C_WasherWoman
from src.Characters.TownsFolk.C_Librarian import C_Librarian
from src.Characters.TownsFolk.C_Investigator import C_Investigator
from src.Characters.TownsFolk.C_Chef import C_Chef
from src.Characters.TownsFolk.C_Empath import C_Empath
from src.Characters.TownsFolk.C_FortuneTeller import C_FortuneTeller
from src.Characters.TownsFolk.C_Undertaker import C_Undertaker
from src.Characters.TownsFolk.C_Monk import C_Monk
from src.Characters.TownsFolk.C_RavenKeeper import C_RavenKeeper
from src.Characters.TownsFolk.C_Virgin import C_Virgin
from src.Characters.TownsFolk.C_Slayer import C_Slayer
from src.Characters.TownsFolk.C_Soldier import C_Soldier
from src.Characters.TownsFolk.C_Mayor import C_Mayor
from src.Characters.Outsider.C_Butler import C_Butler
from src.Characters.Outsider.C_Saint import C_Saint
from src.Characters.Outsider.C_Recluse import C_Recluse
from src.Characters.Outsider.C_Drunk import C_Drunk
from src.Characters.Minion.C_Poisoner import C_Poisoner
from src.Characters.Minion.C_Spy import C_Spy
from src.Characters.Minion.C_Baron import C_Baron
from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
from src.Characters.Demon.C_Imp import C_Imp

class Characters(Enum):

    # Townsfolk
    WASHER_WOMAN = C_WasherWoman
    LIBRARIAN = C_Librarian
    INVESTIGATOR = C_Investigator
    CHEF = C_Chef
    EMPATH = C_Empath
    FORTUNE_TELLER = C_FortuneTeller
    UNDERTAKER = C_Undertaker
    MONK = C_Monk
    RAVEN_KEEPER = C_RavenKeeper
    VIRGIN = C_Virgin
    SLAYER = C_Slayer
    SOLDIER = C_Soldier
    MAYOR = C_Mayor
    
    # Outsider
    BUTLER = C_Butler
    SAINT = C_Saint
    RECLUSE = C_Recluse
    DRUNK = C_Drunk

    # Minions
    POISONER = C_Poisoner
    SPY = C_Spy
    BARON = C_Baron
    SCARLET_WOMAN = C_ScarletWoman
    
    # Demon
    IMP = C_Imp



