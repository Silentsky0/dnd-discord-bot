from dnd_bot.database.database_connection import DatabaseConnection
from dnd_bot.database.database_entity import DatabaseEntity


class DatabaseCreature:

    @staticmethod
    def add_creature(x: int = 0, y: int = 0, name: str = 'Creature', hp: int = 0, strength: int = 0,
                     dexterity: int = 0, intelligence: int = 0, charisma: int = 0, perception: int = 0,
                     initiative: int = 0, action_points: int = 0, level: int = 0, money: int = 0,
                     id_game: int = 1, experience: int = 0) -> int | None:
        id_entity = DatabaseEntity.add_entity(name=name, x=x, y=y, id_game=id_game)
        id_creature = DatabaseConnection.add_to_db('INSERT INTO public."Creature" (level, "HP", strength, dexterity, '
                                                   'intelligence, charisma, perception, initiative, action_points, '
                                                   'money, id_entity, experience) VALUES'
                                                   '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                                   (
                                                       level, hp, strength, dexterity, intelligence,
                                                       charisma, perception, initiative, action_points,
                                                       money, id_entity, experience),
                                                   "creature")
        return id_creature

    @staticmethod
    def update_creature(id_creature: int = 0, hp: int = 0, level: int = 0, money: int = 0, experience: int = 0, x: int = 0,
                        y: int = 0) -> None:
        DatabaseConnection.update_object_in_db('UPDATE public."Creature" SET level = (%s), "HP" = (%s), money = (%s), '
                                               'experience = (%s) WHERE id_creature = (%s)',
                                               (level, hp, money, experience, id_creature), "Creature")
        id_entity = DatabaseCreature.get_creature_id_entity(id_creature)
        DatabaseEntity.update_entity(id_entity, x, y)

    @staticmethod
    def get_creature(id_creature: int = 0) -> dict | None:
        pass

    @staticmethod
    def get_creature_items(id_creature) -> list | None:
        pass

    @staticmethod
    def get_creature_id_entity(id_creature: int = 0) -> int | None:
        return DatabaseConnection.get_object_from_db(
            f'SELECT id_entity FROM public."Creature" WHERE id_creature = (%s)',
            (id_creature,), "Creature")
