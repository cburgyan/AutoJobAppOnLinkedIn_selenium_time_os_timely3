import datetime


class CodingTimer:
    def __init__(self, filename):
        self.filename = filename

    def file_interaction(self, filemode, list_of_additions):
        if filemode == "r":
            try:
                with open(self.filename, "r") as file:
                    return file.readlines()
            except Exception as error_message:
                print(f'Something went wrong when trying to open and read {self.filename}:\n{error_message}')
        elif filemode == "a":
            try:
                with open(self.filename, "a") as file:
                    for elem in list_of_additions:
                        file.write(elem)
            except Exception as error_message:
                print(f'Something went wrong when trying to open and append {self.filename}:\n{error_message}')

        elif filemode == "w":
            try:
                with open(self.filename, "w") as file:
                    for elem in list_of_additions:
                        file.write(elem)
            except Exception as error_message:
                print(f'Something went wrong when trying to open and write {self.filename}:\n{error_message}')

        else:
            print(f'The file mode you entered is "{filemode}".'
                  f'\nPlease enter try again and enter "r", "a", or "w".')
        return None

    def start_time(self):
        now = datetime.datetime.now()
        result = f'start {now}\n'
        list_of_additions = [result]
        try:
            with open(self.filename, 'r') as file:
                list_file_lines = file.readlines()
                if list_file_lines != []:
                    last_line_dissected = list_file_lines[-1].split(" ")
                    if "duration" in last_line_dissected or "stop" in last_line_dissected:
                        self.file_interaction("a", list_of_additions)
                    elif "pause" in last_line_dissected or "unpause" in last_line_dissected or "start" in last_line_dissected:
                        print("Could NOT start time because time has ALREADY been started!!")
                    else:
                        print("Something went wrong! Time record is corrupted.")
                else:
                    self.file_interaction("a", list_of_additions)
        except FileNotFoundError as error_message:
            self.file_interaction("a", list_of_additions)

    def pause_time(self):
        now = datetime.datetime.now()
        result = f'pause {now}\n'
        list_of_additions = [result]
        list_file_lines = self.file_interaction("r", [])
        last_line_dissected = list_file_lines[-1].split(" ")
        if "unpause" in last_line_dissected or "start" in last_line_dissected:
            self.file_interaction("a", list_of_additions)
        elif "pause" in last_line_dissected:
            print("Could NOT pause time because time was ALREADY paused!!")
        elif "duration" in last_line_dissected:
            print("Could NOT pause time because time has NOT been started yet!!")
        else:
            print("Something went wrong! Time record is corrupted.")

    def unpause_time(self):
        now = datetime.datetime.now()
        result = f'unpause {now}\n'
        list_of_additions = [result]
        list_file_lines = self.file_interaction("r", [])
        last_line_dissected = list_file_lines[-1].split(" ")
        if "pause" in last_line_dissected:
            self.file_interaction("a", list_of_additions)
        elif "unpause" in last_line_dissected or "start" in last_line_dissected:
            print("Time was ALREADY unpaused!!")
        elif "duration" in last_line_dissected:
            print("Could NOT unpause time because time has NOT been started yet!!")
        else:
            print("Something went wrong! Time record is corrupted.")

    def create_datetime(self, day1, time1):
        time1 = time1.replace("\n", "")
        return datetime.datetime.fromisoformat(f'{day1} {time1}')

    def stop_time(self):
        now = datetime.datetime.now()
        result = "stop " f'{now}\n'
        list_of_file_additions = [result]

        list_file_lines = self.file_interaction("r", [])
        prev_line = "stop"
        time_of_prev_line = now
        duration = now - now
        add_a_stop = True
        found_start = False

        for line in list_file_lines[::-1]:
            line_dissected = line.split(" ")
            if "start" in line_dissected:
                if prev_line == "pause" or prev_line == "stop":
                    duration += time_of_prev_line - self.create_datetime(line_dissected[1], line_dissected[2])
                else:
                    print('Found "start" but something went wrong!!')
                    add_a_stop = False
                found_start = True
                break
            elif "unpause" in line_dissected:
                if prev_line == "pause" or prev_line == "stop":
                    time_of_current_line = self.create_datetime(line_dissected[1], line_dissected[2])
                    duration += time_of_prev_line - time_of_current_line
                    time_of_prev_line = time_of_current_line
                    prev_line = "unpause"
            elif "pause" in line_dissected:
                time_of_prev_line = self.create_datetime(line_dissected[1], line_dissected[2])
                prev_line = "pause"
            elif "stop" in line_dissected or "duration" in line_dissected:
                print("Could NOT stop time because the time has NOT been started yet!!")
                add_a_stop = False
                break
            else:
                print("Something went wrong!")
                print(f'No "stop" was added because of the line: "{line_dissected}"')
                add_a_stop = False
                break

        if add_a_stop:
            if found_start:
                list_of_file_additions.append(f'duration {duration}\n')
                self.file_interaction("a", list_of_file_additions)



