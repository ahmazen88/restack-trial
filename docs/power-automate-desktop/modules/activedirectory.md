# Active Directory

Connect to AD and manage users, groups, and directory objects.

This page documents every **native action** in this group (15 items).

## Actions

### Close connection

- **Inventory id:** `activedirectory/close-connection`
- **Kind:** native-action
- **Purpose:** Closes connection.
- **Key inputs:** `Parent directory entry` (Active Directory entry)
- **Produces:** None listed
- **Exceptions:** none listed
- **Microsoft Learn:** [Close connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#closeconnection)

### Connect to server

- **Inventory id:** `activedirectory/connect-to-server`
- **Kind:** native-action
- **Purpose:** Connects to an Active Directory server.
- **Key inputs:** `LDAP path` (Text value); `Use authentication` (Boolean value); `Username` (Text value); `Password` (Direct encrypted input or Text value); `Authentication type` (None, Secure, Encryption, Secure sockets layer, Read-only server, Anonymous, Fast bind, Signing, Sealing, Delegation, Server bind)
- **Produces:** `ParentDirectoryEntry` (Active Directory entry)
- **Exceptions:** `Authentication error`; `Unauthorized access`; `The server isn't operational`; `Invalid operation`; `Active Directory error`
- **Microsoft Learn:** [Connect to server](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#connecttoserveraction)

### Create group

- **Inventory id:** `activedirectory/create-group`
- **Kind:** native-action
- **Purpose:** Creates group.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Group name` (Text value); `Location` (Text value; optional); `Description` (Text value; optional); `Group scope` (Local, Global, Universal); `Group type` (Security, Distribution)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object already exists`; `Active Directory error`
- **Microsoft Learn:** [Create group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#creategroup)

### Create object

- **Inventory id:** `activedirectory/create-object`
- **Kind:** native-action
- **Purpose:** Creates object.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Location` (Text value; optional); `Object type` (Computer, Organizational unit); `Object name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object already exists`; `Invalid attribute syntax`; `Active Directory error`
- **Microsoft Learn:** [Create object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#createobject)

### Create user

- **Inventory id:** `activedirectory/create-user`
- **Kind:** native-action
- **Purpose:** Creates user.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Location` (Text value; optional); `First name` (Text value); `Initials` (Text value; optional); `Last name` (Text value; optional); `Username` (Text value); `Password` (Direct encrypted input or Text value); `Password never expires` (Boolean value); `Disabled account` (Boolean value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object already exists`; `Couldn't set or update password`; `Active Directory error`
- **Microsoft Learn:** [Create user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#createuser)

### Delete object

- **Inventory id:** `activedirectory/delete-object`
- **Kind:** native-action
- **Purpose:** Deletes object.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Active Directory error`
- **Microsoft Learn:** [Delete object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#deleteobject)

### Get group info

- **Inventory id:** `activedirectory/get-group-info`
- **Kind:** native-action
- **Purpose:** Reads group info into a flow variable.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value)
- **Produces:** `GroupInfo` (Group info)
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Active Directory error`
- **Microsoft Learn:** [Get group info](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#getgroupinfo)

### Get group members

- **Inventory id:** `activedirectory/get-group-members`
- **Kind:** native-action
- **Purpose:** Reads group members into a flow variable.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value)
- **Produces:** `GroupMembers` (List of Group members)
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Active Directory error`
- **Microsoft Learn:** [Get group members](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#getgroupmembers)

### Get user info

- **Inventory id:** `activedirectory/get-user-info`
- **Kind:** native-action
- **Purpose:** Reads user info into a flow variable.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value)
- **Produces:** `UserInfo` (User info)
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Active Directory error`
- **Microsoft Learn:** [Get user info](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#getuserinfo)

### Modify group

- **Inventory id:** `activedirectory/modify-group`
- **Kind:** native-action
- **Purpose:** Modifies a group in the Active Directory.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value); `Operation` (Rename group, Delete group, Add user, Remove user); `New name` (Text value); `User distinguished name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Object already exists`; `Active Directory error`
- **Microsoft Learn:** [Modify group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#modifygroupaction)

### Modify user

- **Inventory id:** `activedirectory/modify-user`
- **Kind:** native-action
- **Purpose:** Modify a user in the Active Directory.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value); `Operation` (Enable/disable user, Rename user, Delete user, Reset password); `Enable user` (Boolean value); `New name` (Text value); `New password` (Direct encrypted input or Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Object already exists`; `Invalid attribute syntax`; `Active Directory error`; `Couldn't set or update password`
- **Microsoft Learn:** [Modify user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#modifyuseraction)

### Move object

- **Inventory id:** `activedirectory/move-object`
- **Kind:** native-action
- **Purpose:** Moves object.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value); `Move to location` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Active Directory error`; `Location can't be empty`
- **Microsoft Learn:** [Move object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#moveobject)

### Rename object

- **Inventory id:** `activedirectory/rename-object`
- **Kind:** native-action
- **Purpose:** Renames object.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value); `New name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Object already exists`; `Active Directory error`
- **Microsoft Learn:** [Rename object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#renameobject)

### Unlock user

- **Inventory id:** `activedirectory/unlock-user`
- **Kind:** native-action
- **Purpose:** Unlocks an Active Directory user.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Active Directory error`
- **Microsoft Learn:** [Unlock user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#unlockuser)

### Update user info

- **Inventory id:** `activedirectory/update-user-info`
- **Kind:** native-action
- **Purpose:** Updates user info.
- **Key inputs:** `Parent directory entry` (Active Directory entry); `Distinguished name` (Text value); `Display name` (Text value; optional); `First name` (Text value; optional); `Initials` (Text value; optional); `Last name` (Text value; optional); `Title` (Text value; optional); `The email of the user` (Text value; optional); `The company of the user` (Text value; optional); `Telephone number` (Text value; optional); `Extension` (Text value; optional); `City` (Text value; optional); `Postal code` (Text value; optional); `State` (Text value; optional); `Country` (Afghanistan, Åland Islands, Albania, Algeria, American Samoa, Andorra, Angola, Anguilla, Antarctica, Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bermuda, Bhutan, State of Bolivia Plurinational, Bonaire, Bosnia and Herzegovina, Botswana, Bouvet Island, Brazil, British Indian Ocean Territory, Brunei Darussalam, Bulgaria, Burkina Faso, Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Cayman Islands, Central African Republic, Chad, Chile, China, Christmas Island, Cocos (Keeling) Islands, Colombia, Comoros, Congo, Democratic Republic of the Congo, Cook Islands, Costa Rica, Côte d'Ivoire, Croatia, Cuba, Curaçao, Cyprus, Czech Republic, Denmark, Djibouti, Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Ethiopia, Falkland Islands, Faroe Islands, Fiji, Finland, France, French Guiana, French Polynesia, French Southern Territories, Gabon, Gambia, Georgia, Germany, Ghana, Gibraltar, Greece, Greenland, Grenada, Guadeloupe, Guam, Guatemala, Guernsey, Guinea, Guinea-Bissau, Guyana, Haiti, Heard Island and McDonald Islands, Holy See, Honduras, Hong Kong Special Administrative Region, Hungary, Iceland, India, Indonesia, Islamic Republic of Iran, Iraq, Ireland, Isle of Man, Israel, Italy, Jamaica, Japan, Jersey, Jordan, Kazakhstan, Kenya, Kiribati, Democratic Peoples Republic of Korea, Republic of Korea, Kuwait, Kyrgyzstan, Lao People's Democratic Republic, Latvia, Lebanon, Lesotho, Liberia, Libya, Liechtenstein, Lithuania, Luxembourg, Macao Special Administrative Region, North Macedonia, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Martinique, Mauritania, Mauritius, Mayotte, Mexico, Micronesia, Moldova, Monaco, Mongolia, Montenegro, Montserrat, Morocco, Mozambique, Myanmar, Namibia, Nauru, Nepal, Netherlands, New Caledonia, New Zealand, Nicaragua, Niger, Nigeria, Niue, Norfolk Island, Northern Mariana Islands, Norway, Oman, Pakistan, Palau, Palestinian Authority, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Pitcairn, Poland, Portugal, Puerto Rico, Qatar, Réunion, Romania, Russia, Rwanda, Saint Barthélemy, Saint Helena, Ascension, Tristan da Cunha, Saint Kitts and Nevis, Saint Lucia, Saint Martin (French part), Saint Pierre and Miquelon, Saint Vincent and the Grenadines, Samoa, San Marino, São Tomé and Príncipe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Sint Maarten (Dutch part), Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, South Georgia and the South Sandwich Islands, South Sudan, Spain, Sri Lanka, Sudan, Suriname, Svalbard and Jan Mayen, Swaziland, Sweden, Switzerland, Syrian Arab Republic, Taiwan, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Tokelau, Tonga, Trinidad and Tobago, Tunisia, Türkiye, Turkmenistan, Turks and Caicos Islands, Tuvalu, Uganda, Ukraine, United Arab Emirates, United Kingdom of Great Britain and Northern Ireland, United States of America, United States Minor Outlying Islands, Uruguay, Uzbekistan, Vanuatu, Bolivarian Republic of Venezuela, Vietnam, Virgin Islands (British), Virgin Islands (U.S.), Wallis and Futuna, Yemen, Zambia, Zimbabwe, None)
- **Produces:** None listed
- **Exceptions:** `Authentication error`; `Invalid operation`; `The server isn't operational`; `Unauthorized access`; `Active Directory entry not found`; `Object doesn't exist on server`; `Couldn't set or update password`; `Active Directory error`
- **Microsoft Learn:** [Update user info](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#updateuserinfo)
