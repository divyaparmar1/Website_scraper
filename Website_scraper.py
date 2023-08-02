import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup
from PIL import Image

def scrape_website():
    url = entry_url.get()
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract title
            title = soup.title.text.strip()

            # Extract paragraphs
            paragraphs = [p.get_text().strip() for p in soup.find_all('p')]

            # Show results
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, f"Title: {title}\n\n")
            text_output.insert(tk.END, "First few paragraphs:\n")
            for paragraph in paragraphs[:5]:
                text_output.insert(tk.END, f"{paragraph}\n\n")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch the URL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "Please enter a valid URL.")

# Create the main application window
app = tk.Tk()
app.title("Website Scraper")

# Add GUI elements
label_url = tk.Label(app, text="Enter URL:")
label_url.pack()
entry_url = tk.Entry(app, width=50)
entry_url.pack()

button_scrape = tk.Button(app, text="Scrape Website", command=scrape_website)
button_scrape.pack()
text_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=20)
text_output.pack()

# Start the main loop
app.mainloop()
