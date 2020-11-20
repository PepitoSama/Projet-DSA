import os
import csv
import email

mail_dir = os.getcwd() + "/maildir" 
csv_dir = os.getcwd() + "/csv"
if(not os.access(csv_dir, os.F_OK)): os.mkdir(csv_dir)

def produce_csv():
    total_mail_count = get_total_mail_count()
    writed_mail_count = 0
    print("File output location : {}".format(csv_dir + "/mail.csv"))
    with open(csv_dir + "/mail.csv", "w") as mail_csv:
        writer = csv.writer(mail_csv)
        write_header(writer)
        for directory, sub_directories, files in os.walk(mail_dir):
            for f in files:
                refresh_progress_bar(writed_mail_count, total_mail_count)
                [headers, msg] = read_mail(os.path.join(directory, f))
                writer.writerow([
                    headers['To'],
                    headers['From'],
                    headers['Subject'],
                    headers['Date'],
                    msg])
                writed_mail_count = writed_mail_count + 1

def read_mail(path): 
    with open(path, 'r') as mail:
        msg_str = mail.read()
        headers = email.message_from_string(msg_str)
        msg = email.message_from_string(msg_str).get_payload()
        mail.close()
    return [headers, msg]

def refresh_progress_bar(done_count, todo_count):
    print("Progress : {} (written) / {} (total)".format(done_count, todo_count), end="\r", flush=True)

def write_header(writer):
    writer.writerow(["_T","_F","_S","_D","_C"])

def get_total_mail_count():
    mail_count = 0
    for dir, subs, files in os.walk(mail_dir):
        mail_count = mail_count + len(files)
    return mail_count

def main():
    produce_csv()

if __name__ == "__main__":
    main()