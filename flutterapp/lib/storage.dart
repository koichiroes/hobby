import 'package:flutterapp/habit.dart';

abstract class PersistentStore {
  Future open();

  Future<List<Habit>> insertHabits(List<Habit> habits);

  Future<Habit> updateHabit(Habit habit);

  Future<HabitStroke> insertHabitStroke(HabitStroke stroke);

  Future<HabitStroke> updateHabitStroke(HabitStroke stroke);

  Future<HabitStroke> getHabitStroke(HabitStroke stroke);

  Future close();
}

class SQLitePersistentStore extends PersistentStore {
  Future open() async {}

  Future<List<Habit>> insertHabits(List<Habit> habits) async {}

  Future<Habit> updateHabit(Habit habit) async {}

  Future<HabitStroke> insertHabitStroke(HabitStroke stroke) async {}

  Future<HabitStroke> updateHabitStroke(HabitStroke stroke) async {}

  Future<HabitStroke> getHabitStroke(HabitStroke stroke) async {}

  Future close() async {}
}
