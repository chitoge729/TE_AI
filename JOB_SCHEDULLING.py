class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"Job {self.id} - Deadline: {self.deadline}, Profit: {self.profit}"


def schedule_jobs(jobs):
    # Sort jobs based on the profit-to-deadline ratio in descending order
    jobs.sort(key=lambda x: x.profit / x.deadline, reverse=True)

    n = len(jobs)
    max_deadline = max(jobs, key=lambda x: x.deadline).deadline
    schedule = [None] * max_deadline

    for job in jobs:
        # Find a slot in the schedule before the job's deadline
        for i in range(job.deadline - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = job
                break

    return [job for job in schedule if job is not None]


# Get user input for the number of jobs
num_jobs = int(input("Enter the number of jobs: "))

# Get user input for job details (id, deadline, profit)
jobs = []
for i in range(num_jobs):
    job_id = input(f"Enter job {i + 1} ID: ")
    deadline = int(input(f"Enter job {i + 1} deadline: "))
    profit = int(input(f"Enter job {i + 1} profit: "))
    jobs.append(Job(job_id, deadline, profit))

# Schedule the jobs
scheduled_jobs = schedule_jobs(jobs)

# Print the scheduled jobs
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(job)
