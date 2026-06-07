
<h1><i>🎮 The Underground Town</i>: A Fantasy Text-Based Adventure Game</h1>
<p>This Underground Town was inspired from the 80's retro game, Zork, with its fantasy themes and interactive typed commands to commit actions in the game. Players are able to move around in a custom coordinate system with interconnected places, discover different itesm, and solve problems to win the game.
<br><br>
This project showcases object-oriented programming along with several other python techniques and methods. This game was built to not only recreate a puzzle-solving complex text-based adventure game, but to also to showcase object-oriented programming, along with several other python techniques and methods.</p>
<br>

<h2>📁 Repository Structure</h2>
<ul>
<li><strong>MohaleFunction.py</strong></li>
  <ul>
    <li>This holds the code for the game to be run</li>
  </ul>
</li>

<li><strong>exercise.py</strong></li>
  <ul>
    <li>This file was used in order for the all group members to ensure that their github was working correctly.</li>
  </ul>
</li>

<li><strong>responses.json</strong></li>
  <ul>
    <li>Used in MohaleFunction and is a nested dictionary to automate responses to certain actions that the user takes</li>
  </ul>
</li>

<li><strong>actions.json</strong></li>
  <ul>
    <li>Used in MohaleFunction and is a nested dictionary that has options of all actions that can be taken by the player</td></li>
  </ul>
</li>

<li><strong>items.json</strong></li>
  <ul>
    <li>Used in MohaleFunction to generate all items and attributes in the items class; generates different item objects within the game.</td></li>
  </ul>
</li>

<li><strong>places.json</strong></li>
  <ul>
    <li>Used in MohaleFunction to generate all places and attributes in the places class; generates different place objects within the game.</td></li>
  </ul>
</li>
</ul>

<br>

<h2>👥 Python Techniques and Methods</h2>
<ul>
  <li>
    Object-Oriented Programming
    <ul>
      <li>In the Player, Item, Game and Places Classes</li>
    </ul>
  </li>
   <li>
    File Handliing
    <ul>
      <li><pre>with open()</pre></li>
    </ul>
  </li>
   <li>
    JSON Parsing
    <ul>
      <li><pre>json.load()</pre></li>
    </ul>
  </li>
   <li>
    File Handliing
    <ul>
      <li><pre>with open()</pre></li>
    </ul>
  </li>
   <li>
    Regular Expressions
    <ul>
      <li><pre>re.search(), re.escape()</pre></li>
    </ul>
  </li>
  <li>
    File Handliing
    <ul>
      <li><pre>with open()</pre></li>
    </ul>
  </li>
   <li>
    List Comprehensions
    <ul>
      <li>In updatePlayerPosition(), action(), and win() functions</li>
    </ul>
  </li>
  <li>
    File Handliing
    <ul>
      <li><pre>with open()</pre></li>
    </ul>
  </li>
   <li>
    List Comprehensions
    <ul>
      <li>In updatePlayerPosition(), action(), and win() functions</li>
    </ul>
  </li>
  <li>
    File Handliing
    <ul>
      <li><pre>with open()</pre></li>
    </ul>
  </li>
   <li>
    State Management
    <ul>
      <li>For Inventory, Flashlight, Chest, Trapdoor, Painting, and Purple Drink</li>
    </ul>
  </li>
  <li>
    Data-Oriented Programming
    <ul>
      <li>Responses, places, items, and actions all stored in JSON files</li>
    </ul>
  </li>
</ul>

<br>

<h2>🚀 Running the Game</h2>

<blockquote>

Run it in a Python code runner (Visual Studio → (Mac) type
<code>python3 MohaleFunction.py</code> or
<code>python MohaleFunction.py</code> (PC) and make sure to import the
MohaleFunction.py and all JSON files into the same folder along with the
same names as seen in the repository.

We do not use any command line arguments.

</blockquote>

<hr>

<h2>🏆 Objective of the Game</h2>

<p>
The main goal of the game is to explore the map, taking and using items
in the quest to collect two main items.
</p>

<p>
<strong>To win the game, you need to take the diamond egg and the
sorcerer's stone.</strong>
</p>

<hr>

<br>

<h2>🧭 Movement</h2>

<ul>
<li>Move using nearby location names</li>
<li>Move using cardinal directions (north, south, east, west)</li>
<li>Move using relative directions (left, right, forward, back)</li>
</ul>

<p>
The specific movement commands are:
</p>

<pre>
go
walk
move
run
</pre>

<p>
There is a special case location (kitchen and underground entrance)
that can only be moved back and forth using the
<strong>open trapdoor</strong> command.
</p>

<hr>

<br>

<h2>🎒 Items</h2>

<p>
You can use the look command to see any items in the room or a hint of
a potentially hidden one.
</p>

<p>
Many item interactions are available:
</p>

<table>
<tr>
<th>Action</th>
<th>Commands</th>
</tr>

<tr>
<td>Pick Up</td>
<td>take, get, grab, pick</td>
</tr>

<tr>
<td>Open</td>
<td>open, lift</td>
</tr>

<tr>
<td>Use</td>
<td>use, turn on</td>
</tr>

<tr>
<td>Consume</td>
<td>drink</td>
</tr>

</table>

<p>
Check your inventory using:
</p>

<pre>
inventory
inv
</pre>

<hr>

<br>

<h2>❓ Help & Ending the Game</h2>

<ul>
<li><strong>q</strong> or <strong>quit</strong> → End the game</li>
<li><strong>?</strong> or <strong>help</strong> → Display available commands</li>
</ul>

<hr>

<h2>💡 Sample Commands</h2>

<pre>
Move right
turn on flashlight
open chest
walk to living room
lift painting
</pre>

<hr>


<h2>📚 Annotated Bibliography</h2>

<details>
  <summary><strong>Python re.escape() method</strong></summary>

  <p>Python re.escape() method. (n.d.). Tutorial Point. Retrieved May 8, 2026, from https://www.tutorialspoint.com/python/python_re_escape_method.htm</p>

  <p><strong>Used this source to figure out how the re.escape command works so I can use it to handle cases where the input has a space/special keys</strong></p>
</details>

<details>
  <summary><strong>Zork I</strong></summary>

  <p>Zork I. (n.d.). Retrieved May 8, 2026, from http://retinal.dehy.de/docs/doku.php?id=miscellaneous:games:zork_i</p>

  <p><strong>Research on the background of the game and the specific objectives and tasks that occur in the game</strong></p>
</details>

<details>
  <summary><strong>Zork I Map</strong></summary>

  <p>Zork I Map. (n.d.). Untitled. Retrieved May 8, 2026, from https://www.mocagh.org/infocom/zork-map-front.pdf</p>

  <p><strong>Used to base our own map layout to be similar to the original Zork game.</strong></p>
</details>

<details>
  <summary><strong>ZORK I: The Great Underground Empire</strong></summary>

  <p>ZORK I: The Great Underground Empire. (n.d.). MIT. Retrieved May 8, 2026, from https://web.mit.edu/marleigh/www/portfolio/Files/zork/transcript.html</p>

  <p><strong>Shows the actions and what a live run-through of Zork would look like. We based the actions and movement on this transcript.</strong></p>
</details>

<details>
  <summary><strong>Zork I: The Great Underground Empire/Walkthrough</strong></summary>

  <p>Zork I: The Great Underground Empire/Walkthrough. (n.d.). STRATEGYWIKI. Retrieved May 8, 2026, from https://strategywiki.org/wiki/Zork_I:_The_Great_Underground_Empire/Walkthrough</p>

  <p><strong>We based our game progression and the necessities to win on this walkthrough.</strong></p>
</details>

<details>
  <summary><strong>A simple function that scrolls text to the Python console</strong></summary>

  <p>BD103. (2020, December 7). A simple function that scrolls text to the Python console. GithubGist. Retrieved May 8, 2026, from https://gist.github.com/BD103/f89ef60a57aedd68394b38b8f22584d5</p>

  <p><strong>We used this function to make text printed to the console appear one character at a time, and added an optional flag set through the Game class to disable it</strong></p>
</details>

<details>
  <summary><strong>Python Time Module</strong></summary>

  <p>Python Software Foundation. (2000). time — Time access and conversions — Python 3.7.2 documentation. Python.org. Retrieved May 8, 2026, from https://docs.python.org/3/library/time.html</p>

  <p><strong>This was used both in the text scroll and to measure the time it takes for the player to beat the game, using time.sleep() and time.time().</strong></p>
</details>


</table>
