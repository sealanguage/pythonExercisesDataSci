{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter grades to calculate mean/average grades. tyep e to exit\n",
      " - 3.2\n",
      " - 2.85\n",
      " - 3.7\n",
      " - 3.3\n",
      " - 3.0\n",
      " - 2.6\n",
      " - e\n",
      "[3.2, 2.85, 3.7, 3.3, 3.0, 2.6]\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
    "\n",
    "# create an empty list\n",
    "grades = []\n",
    "sum = 0\n",
    "\n",
    "while( True ) :\n",
    "    grade = input(\" enter grades \")\n",
    "    if grade == \"e\" :\n",
    "        break\n",
    "    else :\n",
    "        grade = float(grade)\n",
    "        grades.append(grade)\n",
    "print(grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-2d6c572b037c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mgrade\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m2.0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "grade[1] = 2.0\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter grades to calculate mean/average grades. tyep e to exit\n",
      " enter grades 4.0\n",
      " enter grades 4.0\n",
      " enter grades 4.0\n",
      " enter grades e\n",
      "[4.0, 4.0, 4.0]\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
    "\n",
    "# create an empty list\n",
    "grades = []\n",
    "\n",
    "while( True ) :\n",
    "    grade = input(\" enter grades \")\n",
    "    if grade == \"e\" :\n",
    "        break\n",
    "    else :\n",
    "        grade = float(grade)\n",
    "        grades.append(grade)\n",
    "print(grades)\n",
    "\n",
    "for grade in grades :\n",
    "    sum = sum + grade\n",
    "    average = sum / len(grades)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "grades[1] = 2.1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4.0, 4.0, 4.0]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grades"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11.05\n"
     ]
    }
   ],
   "source": [
    "average = sum / len(grades)\n",
    "print(average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24.066666666666666"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4.0, 4.0, 4.0, 4.0]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grades"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15.05"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "average"
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
      "Enter grades to calculate mean/average grades. tyep e to exit\n",
      " enter grades 4.0\n",
      " enter grades 4.0\n",
      " enter grades 4.0\n",
      " enter grades e\n",
      "[4.0, 4.0, 4.0]\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
    "\n",
    "# create an empty list\n",
    "grades = []\n",
    "\n",
    "while( True ) :\n",
    "    grade = input(\" enter grades \")\n",
    "    if grade == \"e\" :\n",
    "        break\n",
    "    else :\n",
    "        grade = float(grade)\n",
    "        grades.append(grade)\n",
    "print(\"graded: \", grades)\n",
    "\n",
    "for grade in grades :\n",
    "    sum = sum + grade\n",
    "    average = sum /len(grades)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4.0, 4.0, 4.0]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grades"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36.06666666666667"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(len(grades))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "108.2"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter grades to calculate mean/average grades. tyep e to exit\n",
      " enter grades 2.0\n",
      " enter grades 2.0\n",
      " enter grades 2.0\n",
      " enter grades e\n",
      "graded:  [2.0, 2.0, 2.0]\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
    "\n",
    "# create an empty list\n",
    "grades = []\n",
    "\n",
    "while( True ) :\n",
    "    grade = input(\" enter grades \")\n",
    "    if grade == \"e\" :\n",
    "        break\n",
    "    else :\n",
    "        grade = float(grade)\n",
    "        grades.append(grade)\n",
    "print(\"graded: \", grades)\n",
    "\n",
    "for grade in grades :\n",
    "    sum = sum + grade\n",
    "    average = sum /len(grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120.2"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum"
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
