# To ignore the second migration script(for populating the db)
# for tests
from deckbuilder.settings import *


MIGRATION_MODULES = {"deck": None}
