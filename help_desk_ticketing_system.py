class Ticket:
    ticket_counter = 2000

    def __init__(self, staff_id, creator_name, contact_email, issue_description):
        Ticket.ticket_counter += 1
        self.ticket_number = Ticket.ticket_counter
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.issue_description = issue_description
        self.ticket_status = "Open"
        self.response = "Not Yet Provided"

        if "Password Change" in issue_description:
            self.resolve_password_change()

    def resolve_password_change(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New password generated: {new_password}"
        self.ticket_status = "Closed"

    def resolve(self, response):
        self.response = response
        self.ticket_status = "Closed"

    def reopen(self):
        self.ticket_status = "Reopened"

    def display(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.issue_description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.ticket_status}\n")


class TicketStats:
    def __init__(self):
        self.tickets_created = 0
        self.tickets_resolved = 0
        self.tickets_to_solve = 0

    def update_tickets_created(self):
        self.tickets_created += 1
        self.tickets_to_solve += 1

    def update_tickets_resolved(self):
        self.tickets_resolved += 1
        self.tickets_to_solve -= 1

    def display(self):
        print(f"Tickets Created: {self.tickets_created}")
        print(f"Tickets Resolved: {self.tickets_resolved}")
        print(f"Tickets To Solve: {self.tickets_to_solve}\n")


def create_ticket():
    staff_id = input("Enter Staff ID: ")
    creator_name = input("Enter Creator Name: ")
    contact_email = input("Enter Contact Email: ")
    issue_description = input("Enter Issue Description: ")

    return Ticket(staff_id, creator_name, contact_email, issue_description)


def main():
    print("Welcome to the Ticketing System!")
    stats = TicketStats()
    tickets = []

    while True:
        print("1. Create a new ticket")
        print("2. Resolve a ticket")
        print("3. Reopen a ticket")
        print("4. Display ticket information")
        print("5. Display ticket statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_ticket = create_ticket()
            tickets.append(new_ticket)
            stats.update_tickets_created()

        elif choice == 2:
            ticket_number = int(input("Enter the ticket number to resolve: "))
            response = input("Enter the response: ")

            for ticket in tickets:
                if ticket.ticket_number == ticket_number:
                    ticket.resolve(response)
                    stats.update_tickets_resolved()
                    break

        elif choice == 3:
            ticket_number = int(input("Enter the ticket number to reopen: "))

            for ticket in tickets:
                if ticket.ticket_number == ticket_number:
                    ticket.reopen()
                    stats.update_tickets_resolved()
                    break

        elif choice == 4:
            for ticket in tickets:
                ticket.display()

        elif choice == 5:
            stats.display()

        elif choice == 6:
            print("Exiting the Ticketing System...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


