API_design.md

 - users/
   - lists all users in the system
 - [GET] rooms/
   - lists rooms you are part of
 - [POST] rooms/ - Create a room
    - users[] - users to create the room with
 - [GET] rooms/{id}
    - information about the room
 - [GET] rooms/{id}/messages
    - result of messages ordered by newest first
 - [POST] rooms/{id}/messages
    - Make a message



Scenario: Find users

DONE
Given that users exists
When I list all Users
Then I get a list of all users excluding myself

OUT OF SCOPE
Given that user A exists
When I search for user A
Then I get User A back as a result



Scenario: Finding chat

DONE
Given that a couple of chats exists
And I'm not part of any chats
When I list chats
Then I don't see any

DONE
Given that it exists 5 chats
And I'm part of 2 chats of them
When I list chats
I only see the ones I'm part of

DONE
Given that a chat exists that I'm not part of
When I try to access the chat
Then I get a 404

Given that a chat exists that I'm not part of
When I try to access the chats messages
Then I get a 404


Scenario: Start a chat

DONE
Given that I don't have a chat with friend A
When I create a chat with a friend
Then a chat with me and my friend are created

DONE
Given I have a chat with friend A
When I create a chat with friend B
Then I have 2 different chats. One with Friend A and one with friend B

Given I have a chat with friend A
When I try to create a new chat with A
Then the current chat is returned and no new chat is created

Given I have no chat
When I try to create a chat with no members
Then I get an error

OUT OF SCOPE
Given I have a chat with friend A
When I try to create a new chat with A & B
Then I have 1 chat with A
And I have different chat with A & B

Point: Lock down to only one-on-one chats for the moment?






Scenario: Chatting
DONE
Given that I have a room
When I post a message to that room
Then my message is visible to everyone in the room

DONE
Given that I have made a message
When I delete the message
Then the message is deleted from the database

Given that a room has many messages
When I fetch messages
Then the return is paginated

OUT OF SCOPE
Given that I have a message
When I edit the message
Then the message is changed
And it has a flag signifying that the message has changed



OUT OF SCOPE
Scenario: Leaving chat

Given I'm in a chat with A
When I leave
Then the chat is still accessable for A

Question: Should A's see that I have left? 
Or should A never know that I left?
If A writes to me, then the chat will just restart like I never left?
This is only applicable if it is a one-on-one chat
If it is a chat with multiple people then I should be able to leave

Question:
Is leaving the chat part of the US?
Should it be implemented at all?

Conclusion:
Leaving chat is not part of any US
That should be a later concern
Users are not able to leave chats