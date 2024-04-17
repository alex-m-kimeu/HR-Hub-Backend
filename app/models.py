from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

# Define Models
class Employee(db.Model, SerializerMixin):
    __tablename__= 'employees'
    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

    # relationships with review and leave
    reviews = db.relationship('Review', back_populates= 'employee', cascade="all, delete-orphan")
    leave = db.relationship('Leave', back_populates= 'employee', cascade="all, delete-orphan")

    # validation
    @validates('role')
    def validate_role(self, key, role):
        if role != 'employee' and role != 'admin':
            raise ValueError("Category must be either Employee or Admin.")
        return role

    def __repr__(self):
        return f"<Employee {self.name}, {self.email}>"
    

# Review Table
class Review(db.Model, SerializerMixin):
    __tablename__= 'reviews' 
   
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    
    # Foreign Key
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
   
    # Relationship with employee
    employee = db.relationship('Employee', back_populates='reviews')

    @validates('description')
    def validate_description(self, key, description):
         if not 5 <= len(description) <= 100:
             raise ValueError("Description must be between 5 and 100 characters.")
         return description


    def __repr__(self):
         return f"<Review {self.id}, {self.description}>"

class Leave(db.Model, SerializerMixin):
    __tablename__ = "leave"

    id = db.Column(db.Integer,primary_key=True)
    leaveType = db.Column(db.String, nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, nullable=False, default='pending')


    # relationship with employee
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    employee = db.relationship('Employee', back_populates='leave')
   

    #validation
    @validates('status')
    def validate_status(self, key, status):
        if status not in ('accepted', 'rejected', 'pending'):
            raise ValueError("Status must be either 'accepted', 'rejected', or 'pending'")
        return status

    @validates('leaveType')
    def validate_leaveType(self, key, leaveType):
        if leaveType not in ('sick', 'casual', 'vacation'):
            raise ValueError("Invalid Leave Type")
        return leaveType
    
    def __repr__(self):
        return f"<Leave {self.leaveType}, {self.startDate}, {self.endDate}, {self.status}>"
