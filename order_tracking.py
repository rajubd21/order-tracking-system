from abc import ABC, abstractmethod

# 1. Watcher Abstract Base Class
class Watcher(ABC):
    @abstractmethod
    def update(self, status: str):
        pass

# Concrete Watcher 1: Customer's Phone
class CustomerPhone(Watcher):
    def __init__(self, customer_name: str):
        self.customer_name = customer_name

    def update(self, status: str):
        print(f"  SMS to {self.customer_name}: your order is now {status}")

# Concrete Watcher 2: Kitchen Screen
class KitchenScreen(Watcher):
    def update(self, status: str):
        print(f"  Kitchen screen: {status}")

# 2. Order Class (Subject)
class Order:
    def __init__(self):
        self._status = "Placed"
        self._watchers = []

    def attach(self, watcher: Watcher):
        """Add a watcher to the list at any time (Rule 3)."""
        if watcher not in self._watchers:
            self._watchers.append(watcher)

    def detach(self, watcher: Watcher):
        """Remove a watcher from the list at any time (Rule 3)."""
        if watcher in self._watchers:
            self._watchers.remove(watcher)

    def set_status(self, new_status: str):
        # Check if the new status is "Delivered" before notifying, 
        # and remove the kitchen screen from the list if it is.
        if new_status == "Delivered":
            for watcher in list(self._watchers):
                if isinstance(watcher, KitchenScreen):
                    self.detach(watcher)

        self._status = new_status
        print(f"Order is now: {self._status}")
        
        # Notify all remaining watchers at that moment
        for watcher in self._watchers:
            watcher.update(self._status)

# --- Execution matching required output ---
if __name__ == "__main__":
    my_order = Order()
    rahim_phone = CustomerPhone("Rahim")
    kitchen_display = KitchenScreen()

    # Register watchers
    my_order.attach(rahim_phone)
    my_order.attach(kitchen_display)

    # Status Transitions
    my_order.set_status("Cooking")
    print()
    my_order.set_status("Out for delivery")
    print()
    my_order.set_status("Delivered")
