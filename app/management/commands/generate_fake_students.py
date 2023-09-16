from django.core.management.base import BaseCommand
from app.models import Student  # Replace 'app' with your app name
from faker import Faker

class Command(BaseCommand):
    help = 'Generate and insert fake data into the Student model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS('Generating fake student data...'))

        for _ in range(10):  # Generate 10 fake records, adjust as needed
            fake_name = fake.name()
            fake_email = fake.email()
            fake_text = fake.text()

            # Create an instance of Student with fake data and save it
            new_student = Student(name=fake_name, email=fake_email, text=fake_text)
            new_student.save()

        self.stdout.write(self.style.SUCCESS('Fake student data generated and inserted successfully.'))
