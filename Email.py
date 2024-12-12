import tkinter as tk
from tkinter import messagebox
import csv

# File to store data
DATA_FILE = "email_data.csv"

# Keywords to detect spam
SPAM_KEYWORDS = [
    "win", "free", "offer", "credit", "loan", "urgent", "cash", "guarantee", "prize", "reward", "claim",
    "limited", "opportunity", "exclusive", "discount", "hurry", "limited time", "winner", "free gift", "call now",
    "instant", "online", "money", "reward", "freebie", "exclusive offer", "gift card", "phone number", "secure",
    "click here", "now", "submit", "register", "gift", "cash prize", "promotion", "congratulations", "thank you",
    "register now", "don’t miss", "extra cash", "billion", "offer expires", "celebrate", "blocked", "received",
    "prize", "pending", "deposit", "delivery", "verify", "subscribe", "credit card", "sign up", "spam", "pay now",
    "winning", "business", "special offer", "unsecured", "apply now", "winner announcement", "rate", "faster",
    "next", "eligibility", "withdraw", "tracking number", "fake", "unsecured loan", "withdrawal", "transfer",
    "instant money", "fix your loan", "result", "refundable", "payment confirmation", "won", "deal", "resort",
    "check out", "claimed", "instant cash", "solicitation", "scam", "phishing", "contest", "payable",
    "unpaid", "offer ends", "act now", "easy money", "funds", "high rate", "prize money", "cash transfer",
    "secure payment", "lockdown", "school fee", "scheme", "deposit received", "account verification", "SMS",
    "India lottery", "winner selected", "instant access", "secured", "earn free", "withdraw your earnings",
    "free trial", "secure your account", "disposable", "Amazon offer", "Etsy scam", "gift delivery",
    "unpaid balance", "Amazon India", "lost funds", "reward points", "rupees", "Bitcoin", "advance fee",
    "debt settlement", "compensation", "hacked", "email address", "bank details", "personal loan",
    "mutual funds", "business opportunity", "loans", "fund transfer", "fees", "private loan",
    "security clearance", "VIP", "instant approval", "easy credit", "payment notification", "microloan",
    "eligibility check", "forex", "cryptocurrency", "rewards", "emergency loan", "bank transfer",
    "checking balance", "quick deposit", "withdraw earnings", "contest winners", "transfer funds",
    "financial services", "no interest", "make money", "payout", "order now", "reclaim", "blocked account",
    "loan approval", "email received", "urgent request", "transaction alert", "secured line",
    "temporary loan", "security", "pay for goods", "secure transaction", "advance payment", "verified",
    "credit solution", "easy application", "claim your reward", "best offer", "exclusive discounts",
    "survey", "banking service", "payment required", "money order", "personalized offer", "cashback",
    "vacation", "online business", "limited edition", "top up", "change your plan", "reduce debt",
    "secured service", "instant verification", "urgent processing", "full refund", "service provider",
    "exclusively for you", "cash loan", "loan recovery", "limited offer", "scam alert", "phone verification",
    "IMF", "loan settlement", "billing", "verify identity", "business loan", "free insurance", "instant loan",
    "security check", "hardship grant", "exclusive news", "working capital", "sell product", "online course",
    "helpful service", "program offer", "discounted service", "discount coupon", "game prize", "prize draw",
    "referral", "loans for all", "working capital loan", "forex bonus", "loan guarantee", "reliable offers",
    "cash rewards", "special rewards", "unsecured credit", "lowest fee", "unsecured personal loan", 
    "service alerts", "urgent payment", "free product", "premium membership", "work from home",
    "fast approval", "credit evaluation", "low interest rate", "unpaid invoice", "personal gain", "guaranteed win",
    "free trial offer", "free entry", "high return", "one time payment", "multinational", "public alert",
    "account access", "voucher", "earnings opportunity", "free information", "response needed", "no strings attached",
    "balance transfer", "amount due", "faster approval", "down payment", "payment pending", "error in account",
    "missed payment", "loans available", "offer for you", "click link", "savings bond", "free coupon",
    "online deals", "hardship program", "loan approval guaranteed", "limited period offer", "top offer",
    "payment needed", "immediate offer", "money withdrawal", "early access", "earn while you sleep",
    "win now", "bonus points", "deposit now", "money-making opportunity", "mobile verification",
    "return on investment", "redemption", "secured loan", "deposit guarantee", "unsecured money",
    "instant delivery", "limited stock", "exclusive benefit", "service charge", "affiliate marketing",
    "online investment", "lifetime discount", "secure purchase", "loan processing", "only today",
    "call today", "cash immediately", "transaction complete", "financial offer", "free consultation",
    "bank loan", "website deal", "urgent action required", "discount offer", "quick sign up", "loan account",
    "mobile loan", "free mobile recharge", "website offer", "business registration", "money online"
]


# Initialize file with headers if it doesn't exist
def initialize_file():
    try:
        with open(DATA_FILE, mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Email Content", "Classification"])
    except FileExistsError:
        pass

# Function to analyze content and classify it
def analyze_content(content):
    content_lower = content.lower()
    for keyword in SPAM_KEYWORDS:
        if keyword in content_lower:
            return "Spam"
    return "Not Spam"

# Function to save email content and classification to the file
def save_email_content():
    email_content = email_content_text.get("1.0", tk.END).strip()

    if not email_content:
        messagebox.showwarning("Input Error", "Please enter the content of the email.")
        return

    # Analyze content to determine if it's spam
    classification = analyze_content(email_content)

    # Save to file
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email_content, classification])

    messagebox.showinfo("Saved", f"Email content saved as {classification}.")
    email_content_text.delete("1.0", tk.END)

# Function to show the Email Content view
def show_email_content_view():
    email_content_tab.pack(fill="both", expand=True)

# Create main window
root = tk.Tk()
root.title("Email Content Analyzer")
root.geometry("800x600")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the "Show" dropdown menu
show_menu = tk.Menu(menu_bar, tearoff=0)
show_menu.add_command(label="Email Content", command=show_email_content_view)
menu_bar.add_cascade(label="Show", menu=show_menu)

# Email Content View
email_content_tab = tk.Frame(root)
tk.Label(email_content_tab, text="Email Content Analyzer", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(email_content_tab, text="Enter Content of Email:", font=("Arial", 14)).pack(pady=5)
email_content_text = tk.Text(email_content_tab, height=10, width=60, font=("Arial", 12))
email_content_text.pack(pady=10)

save_button = tk.Button(
    email_content_tab,
    text="Save and Analyze Email Content",
    font=("Arial", 14),
    command=save_email_content
)
save_button.pack(pady=20)

# Initialize file
initialize_file()

# Show the default view
show_email_content_view()

# Run the application
root.mainloop()
