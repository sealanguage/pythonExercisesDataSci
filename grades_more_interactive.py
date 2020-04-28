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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
   "execution_count": 40,
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
      "\u001b[0;32m<ipython-input-40-78f8d124eaaf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     11\u001b[0m         \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mchoice\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m6\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     14\u001b[0m         \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
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
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your choice -> \n",
      "Exit program 6 -> \n",
      " -> 6\n"
     ]
    }
   ],
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
