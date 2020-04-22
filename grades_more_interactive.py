{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your choice -> \n",
      "Enter grades 1 -> \n",
      "Exit program 6 _> \n",
      " -> 6\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "object of type 'int' has no len()",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-23-c43feef5227f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0mchoice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\" -> \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mchoice\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mchoice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0misnumeric\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"enter a valid choice\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m         \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: object of type 'int' has no len()"
     ]
    }
   ],
   "source": [
    "grades = []\n",
    "\n",
    "while True :\n",
    "    print(\"Enter your choice -> \")\n",
    "    print(\"Enter grades 1 -> \")\n",
    "    print(\"Exit program 6 _> \")\n",
    "    \n",
    "    choice = int(input(\" -> \"))\n",
    "    \n",
    "    if len(choice) != 1 and choice.isnumeric() :\n",
    "        print(\"enter a valid choice\")\n",
    "        continue\n",
    "        \n",
    "    if int(choice == 6) :\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your choice -> \n",
      "Enter grades - 1 -> \n",
      "Exit program - 6 _>\n",
      "-> 6\n",
      "Enter your choice -> \n",
      "Enter grades - 1 -> \n",
      "Exit program - 6 _>\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-32-39c2bf5f8c3e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Exit program - 6 _>\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m     \u001b[0mchoice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"-> \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mchoice\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/share/virtualenvs/owner1-o7nQsAmR/lib/python3.8/site-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    858\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    859\u001b[0m             )\n\u001b[0;32m--> 860\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/share/virtualenvs/owner1-o7nQsAmR/lib/python3.8/site-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    891\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    892\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 893\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    894\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    895\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "grades = []\n",
    "\n",
    "while True :\n",
    "    print(\"Enter your choice -> \")\n",
    "    print(\"Enter grades - 1 -> \")\n",
    "    print(\"Exit program - 6 _>\")\n",
    "    \n",
    "    choice = input(\"-> \")\n",
    "    \n",
    "    if int(choice == 1) :\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your choice -> \n",
      "Exit program 6 -> \n",
      " -> a\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'a'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-35-78f8d124eaaf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     11\u001b[0m         \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mchoice\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m6\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     14\u001b[0m         \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: 'a'"
     ]
    }
   ],
   "source": [
    "grades = []\n",
    "\n",
    "while True :\n",
    "    print( \"Enter your choice -> \")\n",
    "    print( \"Exit program 6 -> \")\n",
    "    \n",
    "    choice = input(\" -> \")\n",
    "    \n",
    "    if not len(choice) == 1 and choice.isnumeric() :\n",
    "        print(\"enter a valid choice\")\n",
    "        continue\n",
    "    \n",
    "    if int(choice) == 6 :\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  this code works to exit on choice of 6\n",
    "grades = []\n",
    "\n",
    "while True :\n",
    "    print( \"Enter your choice -> \")\n",
    "    print( \"Exit program 6 -> \")\n",
    "    \n",
    "    choice = input(\" -> \")\n",
    "    \n",
    "    if int(choice) == 6 :\n",
    "        break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
