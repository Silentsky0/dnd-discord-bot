from dnd_bot.database.database_connection import DatabaseConnection
from dnd_bot.database.database_entity import DatabaseEntity


class DatabaseCreature:

    @staticmethod
    def add_creature(x: int = 0, y: int = 0, name: str = 'Creature', hp: int = 0, strength: int = 0,
                     dexterity: int = 0, intelligence: int = 0, charisma: int = 0, perception: int = 0,
                     initiative: int = 0, action_points: int = 0, level: int = 0, money: int = 0,
                     id_game: int = 1, experience: int = 0, id_equipment: int = None, creature_class: str = None,
                     description: str = '') -> int | None:
        id_entity = DatabaseEntity.add_entity(name=name, x=x, y=y, id_game=id_game, description=description)
        if creature_class is not None:
            creature_class = creature_class.upper()

        id_creature = DatabaseConnection.add_to_db('INSERT INTO public."Creature" (level, "HP", strength, dexterity, '
                                                   'intelligence, charisma, perception, initiative, action_points, '
                                                   'money, id_entity, experience, id_equipment, class) '
                                                   'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                                   (
                                                       level, hp, strength, dexterity, intelligence,
                                                       charisma, perception, initiative, action_points,
                                                       money, id_entity, experience, id_equipment, creature_class),
                                                   "creature")
        return id_creature

    @staticmethod
    def add_creature_query(x: int = 0, y: int = 0, name: str = 'Creature', hp: int = 0, strength: int = 0,
                           dexterity: int = 0, intelligence: int = 0, charisma: int = 0, perception: int = 0,
                           initiative: int = 0, action_points: int = 0, level: int = 0, money: int = 0,
                           id_game: int = 1, experience: int = 0, id_equipment: int = None, creature_class: str = None,
                           description: str = '', id_entity: int = 0) -> tuple[str, tuple]:
        return 'INSERT INTO public."Creature" (level, "HP", strength, dexterity, ' \
               'intelligence, charisma, perception, initiative, action_points, ' \
               'money, id_entity, experience, id_equipment, class) ' \
               'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', \
            (level, hp, strength, dexterity, intelligence,
             charisma, perception, initiative, action_points,
             money, id_entity, experience, id_equipment, creature_class)

    @staticmethod
    def update_creature(id_creature: int = 0, hp: int = 0, level: int = 0, money: int = 0, experience: int = 0,
                        x: int = 0,
                        y: int = 0) -> None:
        DatabaseConnection.update_object_in_db('UPDATE public."Creature" SET level = (%s), "HP" = (%s), money = (%s), '
                                               'experience = (%s) WHERE id_creature = (%s)',
                                               (level, hp, money, experience, id_creature), "Creature")
        id_entity = DatabaseCreature.get_creature_id_entity(id_creature)
        DatabaseEntity.update_entity(id_entity, x, y)

    @staticmethod
    def get_creature(id_creature: int = 0) -> dict | None:
        query = f'SELECT * FROM public."Creature" WHERE id_creature = (%s)'
        db_t = DatabaseConnection.get_object_from_db(query, (id_creature,), "Creature")
        creature = {'id_creature': db_t[0], 'level': db_t[1], 'hp': db_t[2], 'strength': db_t[3], 'dexterity': db_t[4],
                    'intelligence': db_t[5], 'charisma': db_t[6], 'perception': db_t[7], 'initiative': db_t[8],
                    'action_points': db_t[9], 'money': db_t[10], 'id_entity': db_t[11], 'experience': db_t[12],
                    'id_equipment': db_t[13], 'class': db_t[14]}
        entity = DatabaseEntity.get_entity(creature['id_entity'])
        for key, value in entity.items():
            creature[key] = value
        return creature

    @staticmethod
    def get_creature_id_entity(id_creature: int = 0) -> int | None:
        return DatabaseConnection.get_object_from_db(
            f'SELECT id_entity FROM public."Creature" WHERE id_creature = (%s)',
            (id_creature,), "Creature")[0]
