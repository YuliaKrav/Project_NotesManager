import datetime
import data_former
import file_worker
import data_checker
import data_finder

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

SWOW_ALL_RECORDS_HEADER = "Viewing all of the notes"
ADD_WINDOW_HEADER = "Adding the notes"
DELETE_WINDOW_HEADER = "Deleting the notes"
SAVE_ALL_RECORDS_TO_FILE = "Saving all of the notes"
UPDATE_RECORDS_WINDOW_HEADER = "Updating the list of the notes"
FILTER_RECORDS_WINDOW_HEADER = "Filtering all of the notes"

global number_of_all_notes 


def show_data_message(header, message):
    messagebox.showinfo(header, message)


def delete_data_message():
    delete_window_message = "The note/s  was/were successfully deleted.\n"
    show_data_message(DELETE_WINDOW_HEADER, delete_window_message)


def show_header_notes(tree_view):
    tree_view['columns'] = data_former.DB_HEADER

    # Create columns and headings
    header_list = ['№']
    header_list.extend(data_former.DB_HEADER)
    column_width_list = [50, 100, 120, 300, 250]
    for i in range(0, len(header_list)):
        tree_view.column('#'+str(i), anchor=CENTER,
                         width=column_width_list[i])
        tree_view.heading('#'+str(i), text=header_list[i])


def get_all_notes_from_treeiew(tree_view):
    data = []
    for index in tree_view.get_children():
        values = tree_view.item(index, 'values')
        data.append(values)
    return data

    # Remove


def remove_notes(tree_view, list_for_deleteng):
    global number_of_all_notes
    for note in list_for_deleteng:
        tree_view.delete(note)
        number_of_all_notes -= 1

    # Remove all notes

def remove_all_notes_without_message(tree_view):
    remove_notes(tree_view, tree_view.get_children())

def remove_all_notes(tree_view):

    remove_notes(tree_view, tree_view.get_children())
    delete_data_message()

    # Remove one selected


def remove_one_note(tree_view):
    del_list = []
    del_list.append(tree_view.selection()[0])
    remove_notes(tree_view, del_list)
    all_data = get_all_notes_from_treeiew(tree_view)
    show_notes_on_tree_view(tree_view, all_data)
    delete_data_message()

    # Remove many selected


def remove_many_notes(tree_view):
    remove_notes(tree_view, tree_view.selection())
    all_data = get_all_notes_from_treeiew(tree_view)
    show_notes_on_tree_view(tree_view, all_data)
    delete_data_message()

def save_all_notes(tree_view):
    save_window_message = "All changes were saved.\n"

    all_data = get_all_notes_from_treeiew(tree_view)
    file_worker.write_to_csv_file(all_data)
    show_data_message(SAVE_ALL_RECORDS_TO_FILE, save_window_message)

def show_notes_on_tree_view(tree_view, notes):
# Add data
    global number_of_all_notes
    remove_all_notes_without_message(tree_view)
    number_of_all_notes = 1
    for note in notes:
        # print(note)
        tree_view.insert(parent='', index='end', iid=number_of_all_notes, text=str(
            number_of_all_notes), values=note)
        number_of_all_notes += 1


def show_all_notes(tree_view):
    all_data = []
    for data in file_worker.read_from_csv_file():
        all_data.append(data_former.from_dict_to_value_list(data))
    show_notes_on_tree_view(tree_view, all_data)
    show_all_data_message = f'There is/are {len(all_data)} note/s)'
    show_data_message(SWOW_ALL_RECORDS_HEADER, show_all_data_message)
    


def main_menu():
    global number_of_all_notes 
    number_of_all_notes = 1
    root = Tk()
    root.title("Application Notes")
    root.iconbitmap('iNotebook.png')
    root.geometry("850x650")
    root.resizable(0, 0)

    # Add style
    style = ttk.Style()
    style.theme_use("clam")
    # style.configure("Treeview",
    #     background="silver",
    #     fieldbackground="silver"
    #     )
    style.map("Treeview",
              background=[("selected", "green")]
              )

    show_save_frame = Frame(root)
    show_save_frame.pack(pady=20)

    filter_frame = Frame(root)
    filter_frame.pack(pady=5)

    tree_frame = Frame(root)
    tree_frame.pack(pady=10)

    add_frame = Frame(root)
    add_frame.pack(pady=20)

    delete_frame = Frame(root)
    delete_frame.pack(pady=30)

    update_frame_up = Frame(root)
    update_frame_up.pack(pady=10)
    update_frame_down = Frame(root)
    update_frame_down.pack(pady=0)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_view = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    show_header_notes(tree_view)
    tree_view.pack()
    tree_scroll.config(command=tree_view.yview)

    # Labels
    # main_add_label =  Label(add_frame, text="ADD NEW NOTES")
    id_label = Label(add_frame, text=data_former.DB_HEADER[0])
    id_label.grid(row=0, column=0)

    title_label = Label(add_frame, text=data_former.DB_HEADER[1])
    title_label.grid(row=0, column=1)

    description_label = Label(add_frame, text=data_former.DB_HEADER[2])
    description_label.grid(row=0, column=2)

    id_label = Label(update_frame_up, text=data_former.DB_HEADER[0])
    id_label.grid(row=0, column=0)

    title_label = Label(update_frame_up, text=data_former.DB_HEADER[1])
    title_label.grid(row=0, column=1)

    description_label = Label(update_frame_up, text=data_former.DB_HEADER[2])
    description_label.grid(row=0, column=2)

    from_label = Label(filter_frame, text="  From (yyyy-mm-dd) ")
    from_label.grid(row=0, column=0)

    to_label = Label(filter_frame, text="  To (yyyy-mm-dd) ")
    to_label.grid(row=0, column=5)

    # Entry boxes
    id_add_box = Entry(add_frame, width=10)
    id_add_box.grid(row=1, column=0)

    title_add_box = Entry(add_frame, width=30)
    title_add_box.grid(row=1, column=1)

    description_add_box = Entry(add_frame, width=50)
    description_add_box.grid(row=1, column=2)

    id_update_box = Entry(update_frame_up, width=10)
    id_update_box.grid(row=1, column=0)

    title_update_box = Entry(update_frame_up, width=30)
    title_update_box.grid(row=1, column=1)

    description_update_box = Entry(update_frame_up, width=50)
    description_update_box.grid(row=1, column=2)

    from_year_box = Entry(filter_frame, width=5)
    from_year_box.grid(row=0, column=2)
    from_month_box = Entry(filter_frame, width=3)
    from_month_box.grid(row=0, column=3)
    from_day_box = Entry(filter_frame, width=3)
    from_day_box.grid(row=0, column=4)

    to_year_box = Entry(filter_frame, width=5)
    to_year_box.grid(row=0, column=6)
    to_month_box = Entry(filter_frame, width=3)
    to_month_box.grid(row=0, column=7)
    to_day_box = Entry(filter_frame, width=3)
    to_day_box.grid(row=0, column=8)

    reg_number = filter_frame.register(data_checker.check_symbol_digit)
    from_year_box.config(validate="key", validatecommand=(reg_number, "%P"))
    from_month_box.config(validate="key", validatecommand=(reg_number, "%P"))
    from_day_box.config(validate="key", validatecommand=(reg_number, "%P"))
    to_year_box.config(validate="key", validatecommand=(reg_number, "%P"))
    to_month_box.config(validate="key", validatecommand=(reg_number, "%P"))
    to_day_box.config(validate="key", validatecommand=(reg_number, "%P"))

    # Add note
    def add_note():
        add_window_empty_message = "There is no possibilities to add notes. Not all fields are filled."
        add_window_message = "The note  was successfully added.\n"

        if not data_checker.check_data_empty_at_least_one(id_add_box.get(), title_add_box.get(), description_add_box.get()):
            show_data_message(ADD_WINDOW_HEADER, add_window_empty_message)
            return

        global number_of_all_notes
        result_line = []
        result_line.append(id_add_box.get())
        result_line.append(title_add_box.get())
        result_line.append(description_add_box.get())
        result_line.append(data_former.get_datetime_now())

        tree_view.insert(parent='', index='end', iid=number_of_all_notes, text=str(
            number_of_all_notes), values=result_line)
        number_of_all_notes += 1

        show_data_message(ADD_WINDOW_HEADER, add_window_message)

        # Clear the boxes
        id_add_box.delete(0, END)
        title_add_box.delete(0, END)
        description_add_box.delete(0, END)

    # Update notes

    def select_note():
        # Clear the boxes
        id_update_box.delete(0, END)
        title_update_box.delete(0, END)
        description_update_box.delete(0, END)

        selected_number = tree_view.focus()
        values = tree_view.item(selected_number, 'values')

        id_update_box.insert(0, values[0])
        title_update_box.insert(0, values[1])
        description_update_box.insert(0, values[2])

    def update_note():
        result_line = []
        result_line.append(id_update_box.get())
        result_line.append(title_update_box.get())
        result_line.append(description_update_box.get())
        result_line.append(data_former.get_datetime_now())

        selected_number = tree_view.focus()
        tree_view.item(selected_number, text=str(
            selected_number), values=result_line)

        tree_view.insert(parent='', index='end', iid=number_of_all_notes, text=str(
            number_of_all_notes), values=result_line)
        id_update_box.delete(0, END)
        title_update_box.delete(0, END)
        description_update_box.delete(0, END)
        update_window_message = "The note  was successfully updated.\n"
        show_data_message(UPDATE_RECORDS_WINDOW_HEADER, update_window_message)

    # Filter notes
    def filter_all_notes():
        filter_window_empty_message = "There is no possibilities to filter notes. Not all fields are filled."
        if not data_checker.check_data_empty_at_least_one(from_year_box.get(), from_month_box.get(), from_day_box.get(), 
        to_year_box.get(), to_month_box.get(), to_day_box.get()):
            show_data_message(ADD_WINDOW_HEADER, filter_window_empty_message)
            return

        hour_max = 23
        min_max = 59
        sec_max = 59
        date1 = datetime.datetime(int(from_year_box.get()), int(
            from_month_box.get()), int(from_day_box.get()))
        date2 = datetime.datetime(int(to_year_box.get()), int(
            to_month_box.get()), int(to_day_box.get()), hour_max, min_max, sec_max)
        all_data = data_finder.filter_data(
            date1, date2, get_all_notes_from_treeiew(tree_view))
        show_notes_on_tree_view(tree_view, all_data)
        filter_window_message = "The note/s  was/were successfully filtered.\n"
        show_data_message(FILTER_RECORDS_WINDOW_HEADER, filter_window_message)

    # Buttons
    # Add Buttons
    show_all_records_button = Button(
        show_save_frame, width=50, text="Show all notes", command=lambda: show_all_notes(tree_view))
    show_all_records_button.grid(row=0, column=0)

    save_all_records_button = Button(
        show_save_frame, width=50, text="Save all notes", command=lambda: save_all_notes(tree_view))
    save_all_records_button.grid(row=0, column=1)

    filter_records_button = Button(
        filter_frame, width=30, text="Filter notes", command=filter_all_notes)
    filter_records_button.grid(row=0, column=9)

    add_record_button = Button(
        add_frame, width=20, text="Add note", command=add_note)
    add_record_button.grid(row=1, column=4)

    # Remove Buttons

    remove_all_records_button = Button(
        delete_frame, width=30, text="Remove ALL notes", command=lambda: remove_all_notes(tree_view))
    remove_all_records_button.grid(row=0, column=0)

    remove_one_record_button = Button(
        delete_frame, width=30, text="Remove selected note", command=lambda: remove_one_note(tree_view))
    remove_one_record_button.grid(row=0, column=1)

    remove_many_record_button = Button(
        delete_frame, width=30, text="Remove all selected note", command=lambda: remove_many_notes(tree_view))
    remove_many_record_button.grid(row=0, column=2)

    # Update Buttons
    select_update_button = Button(
        update_frame_down, width=25, text="Select note", command=select_note)
    select_update_button.grid(row=2, column=0)

    update_button = Button(update_frame_down, width=25,
                           text="Update note", command=update_note)
    update_button.grid(row=2, column=2)

    root.mainloop()


main_menu()
