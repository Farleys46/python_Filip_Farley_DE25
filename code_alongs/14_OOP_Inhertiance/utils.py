from numbers import Number

def validate_positive_number(value) -> None:
        if not isinstance (value, Number):
            raise TypeError(f"Your value must be a number not a {type(value)}")
        
        if value < 0:
            raise ValueError(f"Value cant be negative must be positive, not  {value}")