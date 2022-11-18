{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u1bd994xrHUq",
        "outputId": "003f3597-bd74-49f7-947c-f3f1fee0e996"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2401\n"
          ]
        }
      ],
      "source": [
        "a = 7\n",
        "b = 4\n",
        "c = a**b\n",
        "print (c)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Hi there Sam!\"\n",
        "t = s.split()\n",
        "print (t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K_jYyfajrOUd",
        "outputId": "7a2cbc63-6a72-45a7-8303-0225e18e1ffd"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hi', 'there', 'Sam!']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "s = \"Hi there dad\"\n",
        "t = s.split()\n",
        "print (t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aEpAr8hErQIN",
        "outputId": "34c57a52-5ca6-4694-9986-6ad4f37a68a3"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hi', 'there', 'dad']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "planet = \"Earth\"\n",
        "diameter = 12742\n",
        "print (f\"The diameter of {planet} is {diameter} kilometers\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VvdDZKsFrSDu",
        "outputId": "157f6b0b-def9-492a-933b-d308cb144bc7"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The diameter of Earth is 12742 kilometers\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('The diameter of {planet} is {diameter} kilometers.'.format(planet='Earth', diameter='12742'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gdf7FpRxrUWD",
        "outputId": "0baa1a4b-7269-4fb1-edf9-dd342b942fd1"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The diameter of Earth is 12742 kilometers.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]"
      ],
      "metadata": {
        "id": "7oFuc70qreoO"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "l = lst[3][1][2]\n",
        "print(l)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bAv8TdwKrg0F",
        "outputId": "897f77b6-6ab4-4828-8640-1d3a1d05092d"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['hello']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}"
      ],
      "metadata": {
        "id": "RI_7wqugrjL-"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(d['k1'][3][\"tricky\"][3]['target'][3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X8eoSttrrltW",
        "outputId": "11fd8d03-a9fd-4a43-952e-057ccda895bc"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "s = \"user@domain.com\"\n",
        "def grabDomain(s):\n",
        "    myString = \"\"\n",
        "    found = False\n",
        "    for i in string:\n",
        "        if(found):\n",
        "            myString = myString + i\n",
        "            \n",
        "        if(i == \"@\"):\n",
        "            \n",
        "            found = True\n",
        "            \n",
        "    return myString\n",
        "    "
      ],
      "metadata": {
        "id": "pW6bA2GxrnhI"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(grabDomain(s))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 287
        },
        "id": "xjT4YZiyrscd",
        "outputId": "b31370ed-1018-462c-d4d9-bec86db8fe2c"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-11-ddf386e70788>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgrabDomain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-10-390e0399f83b>\u001b[0m in \u001b[0;36mgrabDomain\u001b[0;34m(s)\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mmyString\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mfound\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mstring\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m         \u001b[0;32mif\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfound\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m             \u001b[0mmyString\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmyString\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'string' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization."
      ],
      "metadata": {
        "id": "9dxztpN-rvTe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def findDog(st):\n",
        "    if 'dog' in st.lower():\n",
        "        print(\"True\")\n",
        "    else:\n",
        "        print(\"False\")\n",
        "\n",
        "st = \"Is there a dog here?\"\n",
        "findDog(st)\n",
        "True"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bI-AIT1Gry3T",
        "outputId": "da492b15-98ec-419a-de12-c807d0fc7d5e"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "findDog('Is there a dog here?')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KW2wmr9Mr2Q_",
        "outputId": "12b848d5-5544-4e8b-ab8c-8e5854cf240a"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def countFound(string , searchString):\n",
        "  count = 0\n",
        "  for i in range(len(string)):\n",
        "        if(string[i:i+len(searchString)] == searchString):\n",
        "            count = count + 1\n",
        "  return count"
      ],
      "metadata": {
        "id": "NJfEWTqCr33F"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(countFound(\"Barking dog is a dog\" , \"dog\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YTzBXDpLr6B_",
        "outputId": "719f4e67-e141-473a-dbbb-e6097432251f"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Problem\n",
        "You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: \"No ticket\", \"Small ticket\", or \"Big Ticket\". If your speed is 60 or less, the result is \"No Ticket\". If speed is between 61 and 80 inclusive, the result is \"Small Ticket\". If speed is 81 or more, the result is \"Big Ticket\". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases."
      ],
      "metadata": {
        "id": "Wp2XvxtPr79H"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def caught_speeding(speed, is_birthday):\n",
        "    \n",
        "    if is_birthday:\n",
        "        speeding = speed - 5\n",
        "    else:\n",
        "        speeding = speed\n",
        "    \n",
        "    if speeding > 80:\n",
        "        return 'Big Ticket'\n",
        "    elif speeding > 60:\n",
        "        return 'Small Ticket'\n",
        "    else:\n",
        "        return 'No Ticket'"
      ],
      "metadata": {
        "id": "Fe7ko4hCr_8y"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def caught_speeding(speed, is_birthday):\n",
        "    pass"
      ],
      "metadata": {
        "id": "CmXRtB-IsCWM"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "caught_speeding(81,True)"
      ],
      "metadata": {
        "id": "dosxgLiosEnj"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "caught_speeding(81,False)"
      ],
      "metadata": {
        "id": "k1zYXy7usGn5"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create two dictionaries in Python:\n",
        "\n",
        "First one to contain fields as Empid, Empname, Basicpay\n",
        "\n",
        "Second dictionary to contain fields as DeptName, DeptId.\n",
        "\n",
        "Combine both dictionaries."
      ],
      "metadata": {
        "id": "0tcbruubsKYG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def Merge(dict1, dict2):\n",
        "    return(dict2.update(dict1))\n",
        " \n",
        " \n",
        "dict1 = {'Empid': 'E1', 'Empname': 'Harshini',  'Basicpay': 500000}\n",
        "dict2 = {'DeptName': 'IT', 'DeptId': 'IT55'}\n",
        " \n",
        "print(Merge(dict1, dict2))\n",
        " \n",
        "print(dict2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "su2uxcDMsMBy",
        "outputId": "8a2a9218-cab6-4c24-9eb9-d0597018c5d6"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "None\n",
            "{'DeptName': 'IT', 'DeptId': 'IT55', 'Empid': 'E1', 'Empname': 'Harshini', 'Basicpay': 500000}\n"
          ]
        }
      ]
    }
  ]
}