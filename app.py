from sqlalchemy.orm import Session
from database import SessionLocal
from classes import SwimmerService, CoachService

def main():
    db = SessionLocal()
    swimmer_service = SwimmerService(db)
    coach_service = CoachService(db)

    try:
        while True:
            print("Choose an option:")
            print("1. Add a new swimmer")
            print("2. Add a new coach")
            print("3. List all swimmers")
            print("4. List all coaches")
            print("5. Update swimmer details")
            print("6. Update coach details")
            print("7. Delete a swimmer")
            print("8. Delete a coach")
            print("9. Assign a swimmer to a coach")
            print("10. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                name = input("Name: ")
                age = int(input("Age: "))
                style = input("Style: ")
                best_lap = input("Best Lap: ")
                swimmer = swimmer_service.create_swimmer(name, age, style, best_lap)
                print(f"Swimmer {swimmer.name} added with ID {swimmer.id}")

            elif choice == '2':
                name = input("Name: ")
                age = int(input("Age: "))
                swimmer_id = int(input("Swimmer ID to be allocated (or leave blank for none): ") or 0)
                coach = coach_service.create_coach(name, age, swimmer_id if swimmer_id else None)
                if coach:
                    print(f"Coach {coach.name} added with ID {coach.id}")
                else:
                    print(f"Invalid swimmer ID {swimmer_id}")

            elif choice == '3':
                swimmers = swimmer_service.list_swimmers()
                for swimmer in swimmers:
                    print(f"ID: {swimmer.id}, Name: {swimmer.name}, Age: {swimmer.age}, Style: {swimmer.style}, Best Lap: {swimmer.best_lap}")

            elif choice == '4':
                coaches = coach_service.list_coaches()
                for coach in coaches:
                    print(f"ID: {coach.id}, Name: {coach.name}, Age: {coach.age}, Swimmer ID: {coach.swimmer_id}")

            elif choice == '5':
                swimmer_id = int(input("Swimmer ID to update: "))
                name = input("New Name (leave blank to skip): ") or None
                age = input("New Age (leave blank to skip): ")
                age = int(age) if age else None
                style = input("New Style (leave blank to skip): ") or None
                best_lap = input("New Best Lap (leave blank to skip): ") or None
                swimmer = swimmer_service.update_swimmer(swimmer_id, name, age, style, best_lap)
                if swimmer:
                    print(f"Swimmer {swimmer.name} updated.")
                else:
                    print("Swimmer not found.")

            elif choice == '6':
                coach_id = int(input("Coach ID to update: "))
                name = input("New Name (leave blank to skip): ") or None
                age = input("New Age (leave blank to skip): ")
                age = int(age) if age else None
                swimmer_id = input("New Swimmer ID (leave blank to skip): ")
                swimmer_id = int(swimmer_id) if swimmer_id else None
                coach = coach_service.update_coach(coach_id, name, age, swimmer_id)
                if coach:
                    print(f"Coach {coach.name} updated.")
                else:
                    print("Coach not found.")

            elif choice == '7':
                swimmer_id = int(input("Swimmer ID to delete: "))
                if swimmer_service.delete_swimmer(swimmer_id):
                    print("Swimmer deleted.")
                else:
                    print("Swimmer not found.")

            elif choice == '8':
                coach_id = int(input("Coach ID to delete: "))
                if coach_service.delete_coach(coach_id):
                    print("Coach deleted.")
                else:
                    print("Coach not found.")

            elif choice == '9':
                coach_id = int(input("Coach ID: "))
                swimmer_id = int(input("Swimmer ID: "))
                coach = coach_service.assign_swimmer(coach_id, swimmer_id)
                if coach:
                    print(f"Coach {coach.name} is now assigned to swimmer ID {swimmer_id}.")
                else:
                    print("Invalid coach or swimmer ID.")

            elif choice == '10':
                break
            else:
                print("Invalid choice, please try again.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
