{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter string: string: hi out there in tv land soo goood for outdoors\n",
      "enter a letter: o\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "#  loop through a sentence for each letter\n",
    "#  compare each letter to a user input letter\n",
    "#    if true, increment the counter\n",
    "#    return the counter\n",
    "\n",
    "\n",
    "str = input(\"enter string: \")\n",
    "char = input(\"enter a letter: \")\n",
    "counter = 0\n",
    "\n",
    "for letter in str :\n",
    "    if letter == char :\n",
    "#         print(\"letter = char\")\n",
    "        counter = counter + 1\n",
    "print(counter)    \n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter string: Last Checkpoint: Last Thursday at 7:36 PM\n",
      "entr character to search: t\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "name = input(\"enter string: \")\n",
    "char = input(\"entr character to search: \")\n",
    "\n",
    "counter = 0\n",
    "length = len(name)\n",
    "\n",
    "for i in range(0, length) :\n",
    "    if name[i].upper() == char.upper() :\n",
    "        counter = counter + 1\n",
    "        \n",
    "print(counter)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counter\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a string: Hi There Big Boy\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n",
      "counter_cap:  0 counter_small:  0\n"
     ]
    }
   ],
   "source": [
    "str = input(\"enter a string: \")\n",
    "counter_small = 0\n",
    "counter_cap = 0\n",
    "length = len(str)\n",
    "\n",
    "for i in range(0, length) :\n",
    "    if str[i].upper() == True :\n",
    "        counter_cap = counter_cap + 1\n",
    "        \n",
    "    elif str[i].lower() == True :\n",
    "        counter_small = counter_small + 1\n",
    "    print(\"counter_cap: \", counter_cap, \"counter_small: \", counter_small)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
