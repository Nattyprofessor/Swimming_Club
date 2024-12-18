from sqlalchemy.orm import Session
import models

class SwimmerService:
    def __init__(self, db: Session):
        self.db = db

    def create_swimmer(self, name: str, age: int, style: str, best_lap: str):
        new_swimmer = models.Swimmer(name=name, age=age, style=style, best_lap=best_lap)
        self.db.add(new_swimmer)
        self.db.commit()
        self.db.refresh(new_swimmer)
        return new_swimmer

    def list_swimmers(self):
        return self.db.query(models.Swimmer).all()

    def update_swimmer(self, swimmer_id: int, name: str = None, age: int = None, style: str = None, best_lap: str = None):
        swimmer = self.db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
        if swimmer:
            if name:
                swimmer.name = name
            if age:
                swimmer.age = age
            if style:
                swimmer.style = style
            if best_lap:
                swimmer.best_lap = best_lap
            self.db.commit()
            self.db.refresh(swimmer)
            return swimmer
        return None
    
    def delete_swimmer(self, swimmer_id: int):
        swimmer = self.db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
        if swimmer:
            self.db.delete(swimmer)
            self.db.commit()
            return True
        return False

class CoachService:
    def __init__(self, db: Session):
        self.db = db

    def create_coach(self, name: str, age: int, swimmer_id: int):
        # Check if the swimmer ID exists
        swimmer = self.db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
        if swimmer:
            new_coach = models.Coach(name=name, age=age, swimmer_id=swimmer_id)
            self.db.add(new_coach)
            self.db.commit()
            self.db.refresh(new_coach)
            return new_coach
        else:
            return None
        
    def list_coaches(self):
        return self.db.query(models.Coach).all()
    
    def assign_swimmer(self, coach_id: int, swimmer_id: int):
        coach = self.db.query(models.Coach).filter(models.Coach.id == coach_id).first()
        swimmer = self.db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
        if coach and swimmer:
            coach.swimmer_id = swimmer_id
            self.db.commit()
            self.db.refresh(coach)
            return coach
        return None

    def update_coach(self, coach_id: int, name: str = None, age: int = None, swimmer_id: int = None):
        coach = self.db.query(models.Coach).filter(models.Coach.id == coach_id).first()
        if coach:
            if name:
                coach.name = name
            if age:
                coach.age = age
            if swimmer_id:
                swimmer = self.db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
                if swimmer:
                    coach.swimmer_id = swimmer_id
            self.db.commit()
            self.db.refresh(coach)
            return coach
        return None
    
    def delete_coach(self, coach_id: int):
        coach = self.db.query(models.Coach).filter(models.Coach.id == coach_id).first()
        if coach:
            self.db.delete(coach)
            self.db.commit()
            return True
        return False
