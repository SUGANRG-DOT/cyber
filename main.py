html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Cyber Security Complaint Register Portal</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0; padding: 0; background: #f4f7fc;
            display: flex; justify-content: center; align-items: flex-start;
            min-height: 100vh;
            color: #333;
        }
        .container {
            background: white;
            margin: 40px 20px;
            padding: 30px 40px;
            max-width: 700px;
            width: 100%;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center; 
            color: #2a4365; 
            margin-bottom: 25px;
            font-weight: 700;
        }
        h2 {
            color: #2a4365;
            margin-top: 40px;
            margin-bottom: 15px;
            border-bottom: 2px solid #3182ce;
            padding-bottom: 5px;
        }
        label {
            display: block;
            margin-top: 20px;
            margin-bottom: 8px;
            font-weight: 700;
            color: #2d3748;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        input[type="date"],
        select,
        textarea {
            width: 100%;
            padding: 12px 15px;
            font-size: 16px;
            border: 1.5px solid #cbd5e0;
            border-radius: 8px;
            transition: border-color 0.3s ease;
            box-sizing: border-box;
            resize: vertical;
        }
        input[type="text"]:focus,
        input[type="email"]:focus,
        input[type="tel"]:focus,
        input[type="date"]:focus,
        select:focus,
        textarea:focus {
            outline: none;
            border-color: #3182ce;
            box-shadow: 0 0 8px rgba(49,130,206,0.3);
        }
        textarea {
            min-height: 120px;
        }
        input[type="file"] {
            margin-top: 5px;
        }
        button {
            margin-top: 30px;
            background-color: #3182ce;
            color: white;
            font-weight: 700;
            border: none;
            padding: 14px 0;
            width: 100%;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #2c5282;
        }
        .note {
            font-size: 0.95em;
            color: #4a5568;
            margin-bottom: 10px;
        }
        .privacy {
            font-size: 0.9em;
            margin-top: 25px;
            text-align: center;
        }
        .privacy a {
            color: #3182ce;
            text-decoration: none;
            font-weight: 600;
        }
        .privacy a:hover {
            text-decoration: underline;
        }
        .success-message, .error-message {
            background-color: #e6fffa;
            border: 1px solid #81e6d9;
            padding: 15px 20px;
            border-radius: 8px;
            color: #2c7a7b;
            margin-top: 25px;
            box-shadow: 0 2px 8px rgba(44,122,123,0.2);
        }
        .error-message {
            background-color: #fed7d7;
            border-color: #fc8181;
            color: #c53030;
        }
        .complaint-details p {
            line-height: 1.5;
            margin: 6px 0;
            font-size: 1em;
        }
        .view-complaint-form {
            margin-top: 30px;
            border-top: 1px solid #e2e8f0;
            padding-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Cyber Security Complaint Register Portal</h1>

        <h2>Register a Complaint</h2>
        <p class="note">Please fill out this form to register your cyber security complaint. Your information will be handled confidentially.</p>

        <form method="POST" action="/register" enctype="multipart/form-data">
            <label for="name">Name <span style="color: #e53e3e;">*</span></label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name" />

            <label for="email">Email Address <span style="color: #e53e3e;">*</span></label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address" />

            <label for="phone">Phone Number (Optional)</label>
            <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" />

            <label for="category">Complaint Category (Optional)</label>
            <select id="category" name="category">
                <option value="" selected>-- Select a category --</option>
                <option value="Phishing">Phishing</option>
                <option value="Malware">Malware</option>
                <option value="Data Breach">Data Breach</option>
                <option value="Fraud">Fraud</option>
                <option value="Other">Other</option>
            </select>

            <label for="date_incident">Date of Incident (Optional)</label>
            <input type="date" id="date_incident" name="date_incident" />

            <label for="complaint">Complaint Details <span style="color: #e53e3e;">*</span></label>
            <textarea id="complaint" name="complaint" required placeholder="Describe the incident in detail"></textarea>

            <label for="attachment">Attachments (Optional)</label>
            <input type="file" id="attachment" name="attachment" accept=".jpg,.jpeg,.png,.pdf,.doc,.docx,.txt" />

            <button type="submit">Submit Complaint</button>
        </form>

        {% if receipt %}
        <div class="success-message complaint-details">
            <h2>Complaint Registered Successfully!</h2>
            <p><b>Complaint ID:</b> {{ receipt['id'] }}</p>
            <p><b>Name:</b> {{ receipt['name'] }}</p>
            <p><b>Email:</b> {{ receipt['email'] }}</p>
            {% if receipt.get('phone') %}<p><b>Phone:</b> {{ receipt['phone'] }}</p>{% endif %}
            {% if receipt.get('category') %}<p><b>Category:</b> {{ receipt['category'] }}</p>{% endif %}
            {% if receipt.get('date_incident') %}<p><b>Date of Incident:</b> {{ receipt['date_incident'] }}</p>{% endif %}
            <p><b>Complaint:</b> {{ receipt['complaint'] }}</p>
            <p><b>Receipt:</b> Please save this Complaint ID as your proof of registration.</p>
        </div>
        {% endif %}

        <div class="view-complaint-form">
            <h2>View Your Complaint</h2>
            <form method="GET" action="/view">
                <label for="complaint_id">Enter your Complaint ID:</label>
                <input type="text" id="complaint_id" name="complaint_id" required placeholder="e.g. 123e4567-e89b-12d3-a456-426614174000" />
                <button type="submit">View Complaint</button>
            </form>
        </div>

        {% if complaint %}
        <div class="success-message complaint-details" style="margin-top: 30px;">
            <h2>Complaint Details</h2>
            <p><b>Complaint ID:</b> {{ complaint['id'] }}</p>
            <p><b>Name:</b> {{ complaint['name'] }}</p>
            <p><b>Email:</b> {{ complaint['email'] }}</p>
            {% if complaint.get('phone') %}<p><b>Phone:</b> {{ complaint['phone'] }}</p>{% endif %}
            {% if complaint.get('category') %}<p><b>Category:</b> {{ complaint['category'] }}</p>{% endif %}
            {% if complaint.get('date_incident') %}<p><b>Date of Incident:</b> {{ complaint['date_incident'] }}</p>{% endif %}
            <p><b>Complaint:</b> {{ complaint['complaint'] }}</p>
        </div>
        {% endif %}

        {% if error %}
        <div class="error-message">
            <p>{{ error }}</p>
        </div>
        {% endif %}

        <div class="privacy">
            <p>By submitting this form, you agree to our <a href="/privacy-policy" target="_blank" rel="noopener">Privacy Policy</a>.</p>
        </div>
    </div>
</body>
</html>
'''
