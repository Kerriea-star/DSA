"""
A "class" serves as a primary means fir abstracting in object-oriented programming.
In Python, every piece of data is represented as an instance of some class.
A class provides a set of behaviors in the form of "member functions" (also known
as "methods"), with implementations that are common to all instances of that class.
A class also serves as a blueprint for its instances, effectively the way
that state information for each instance is represented in the form of "attributes" (also
known as "fields", "instance variables" or "data members).
"""

# Example: CreditCard Class

"""
The instances defined by the CreditCard class provide a simple model for traditional
credit cards. They have identifying information about the customer, bank, account number, 
credit limit and current balance. The class restricts charges that would cause a card's 
balance to go over its spending limit, but it does not charge interest or late payments.

In a class there are methods defined as functions which have a special parameter namesd
"self", that serves to identify the particular instance upon which a member is invoked
"""

# The self Identifier

"""
In Python, the self identifier plays a key role. In the context of CreditCard
class, there can presumably be many different CreditCard instances, and each must
maintain its own balance, its own credit limit and so on. Therefore, each instance
stores its own instances variables to reflect its current state.

Syntactically, self identifies the instance upon which a method is invoked. For
example, assume that a user of our class has a variable, my_card, that identifies
an instance of the CreditCard class. When the use calls my_card.get_balance(),
the identifier self, within the definition of the get_balance method refers to the card
known as my_card by the caller. The expressionm self._balance refers to an instance
variable, names _balance stored as part of that particular credit card'state.
"""
class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance
        
        The initial balance is zero.

        customer    the name of the customer(e.g., "John Bowman")
        bank        the name of the bank(e.g., "California Savings")
        acnt        the acount identifier(e.g., "5391 0375 9387 5309")
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number(typically stored as a string)."""
        return self._account
    
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit: # if charge would exceed limit
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

"""
We draw attention to the difference between the method signature as declared
within the class versus that used by a caller. For example, from a user's perspective
we have seen that the get_balance method takes zero parameters, yet within
the class definition, self is an explicit parameter. Likewise, the charge method is
declared within the class having two parameters(self and price), even though this
method is called with one parameter, for example, as my_card.charge(200). The
interpretter automatically binds the instance upon which the method is invoked to
the self parameter.
"""