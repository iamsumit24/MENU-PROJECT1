{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7512a97-8c7d-4477-b829-f2c5d085ffa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from twilio.rest import Client\n",
    "\n",
    "def make_phone_call():\n",
    "    # Your Account SID and Auth Token from twilio.com/console\n",
    "    account_sid = 'your_account_sid'\n",
    "    auth_token = 'your_auth_token'\n",
    "    client = Client(account_sid, auth_token)\n",
    "\n",
    "    # Recipient's phone number (include country code) and Twilio phone number\n",
    "    phone_number = input(\"Enter the recipient's phone number (include country code): \")\n",
    "    twilio_phone_number = 'your_twilio_phone_number'\n",
    "    \n",
    "    # The URL that Twilio will request when the call is answered\n",
    "    twiml_url = 'http://demo.twilio.com/docs/voice.xml'\n",
    "\n",
    "    # Making the call\n",
    "    call = client.calls.create(\n",
    "        to=phone_number,\n",
    "        from_=twilio_phone_number,\n",
    "        url=twiml_url\n",
    "    )\n",
    "\n",
    "    print(f\"Call initiated to {phone_number}. SID: {call.sid}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    make_phone_call()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fb2e812-cc23-4e2f-9ef3-eafc2dc93878",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
