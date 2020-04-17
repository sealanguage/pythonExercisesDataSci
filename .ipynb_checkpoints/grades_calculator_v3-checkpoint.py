{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter your choice \n",
      " Enter grades -> 1 \n",
      " Exit program -> 6 \n",
      "6\n"
     ]
    }
   ],
   "source": [
    "grades = []    #initialize an empty list\n",
    "\n",
    "while True :    #this program runs in an infinite loop\n",
    "    print(\" Enter your choice \")\n",
    "    print(\" Enter grades -> 1 \")\n",
    "#     print(\" Delete grades -> 2 \")\n",
    "#     print(\" \")\n",
    "#     print(\" \")\n",
    "    print(\" Exit program -> 6 \")\n",
    "    \n",
    "    choice = input(\"\")\n",
    "    \n",
    "    if len(choice != 1) :\n",
    "        print( \"enter a valid choice number 1 - 6\")\n",
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
