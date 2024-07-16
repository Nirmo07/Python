def read_feedback(file_names):
    feedback_data = []
    for file_name in file_names:
        try:
            with open(file_name, 'r') as file:
                feedback_data.extend(file.readlines())
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
    return feedback_data

def process_feedback(feedback_data):
    feedback_entries = []
    total_rating = 0
    for entry in feedback_data:
        try:
            name, rest = entry.split(':', 1)
            rating, comment = rest.split('-', 1)
            
            name = name.strip()
            rating = int(rating.strip())
            comment = comment.strip()
            
            feedback_entries.append((name, rating, comment))
            total_rating += rating
        except ValueError:
            print(f"Error processing entry: {entry.strip()}")
    
    total_entries = len(feedback_entries)
    
    if total_entries > 0:
        average_rating = total_rating / total_entries
    else:
        average_rating = 0

    return feedback_entries, total_entries, average_rating, total_rating

def write_summary(feedback_entries, total_entries, average_rating, total_rating, summary_file_name):
    try:
        with open(summary_file_name, 'w') as file:
            file.write(f"Total Feedback Entries: {total_entries}\n")
            file.write(f"Total Rating: {total_rating}\n")
            file.write(f"Average Rating: {average_rating:.2f}\n")
            file.write("\nFeedbacks:\n")
            for name, rating, comment in feedback_entries:
                file.write(f"{name}: {rating} - {comment}\n")
    except IOError as e:
        print(f"Error writing to summary file: {e}")

def main():
    file_names = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt']
    summary_file_name = 'feedback_summary.txt'
    
    feedback_data = read_feedback(file_names)
    
    feedback_entries, total_entries, average_rating, total_rating = process_feedback(feedback_data)
    
    write_summary(feedback_entries, total_entries, average_rating, total_rating, summary_file_name)
    
    print("Feedback summary has been created successfully.")

main()
