# Active Directory

Connect to Active Directory and manage users, groups, and objects.

- Actions in this module: **15**
- Official docs: [Active Directory actions](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory)

## Actions

### Create group

Creates a group in the Active Directory.

Designer name: **Create group**. Official reference: [Active Directory / Create group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#creategroup).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Group name | Required | Text value | — |
| Location | Optional | Text value | — |
| Description | Optional | Text value | — |
| Group scope | Choice | Local, Global, Universal | Global |
| Group type | Choice | Security, Distribution | Security |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object already exists`, `Active Directory error`.

---

### Get group info

Reads information about a group from the Active Directory server.

Designer name: **Get group info**. Official reference: [Active Directory / Get group info](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#getgroupinfo).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| GroupInfo | Group info |

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Active Directory error`.

---

### Get group members

Reads the members of a group in the Active Directory.

Designer name: **Get group members**. Official reference: [Active Directory / Get group members](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#getgroupmembers).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| GroupMembers | List of Group members |

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Active Directory error`.

---

### Modify group

Modifies a group in the Active Directory.

Designer name: **Modify group**. Official reference: [Active Directory / Modify group](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#modifygroupaction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |
| Operation | Choice | Rename group, Delete group, Add user, Remove user | Rename group |
| New name | Required | Text value | — |
| User distinguished name | Required | Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Object already exists`, `Active Directory error`.

---

### Create object

Creates an object in the Active Directory.

Designer name: **Create object**. Official reference: [Active Directory / Create object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#createobject).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Location | Optional | Text value | — |
| Object type | Choice | Computer, Organizational unit | Computer |
| Object name | Required | Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object already exists`, `Invalid attribute syntax`, `Active Directory error`.

---

### Delete object

Deletes an object in the Active Directory.

Designer name: **Delete object**. Official reference: [Active Directory / Delete object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#deleteobject).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Active Directory error`.

---

### Move object

Moves an object in the Active Directory.

Designer name: **Move object**. Official reference: [Active Directory / Move object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#moveobject).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |
| Move to location | Required | Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Active Directory error`, `Location can't be empty`.

---

### Rename object

Renames an object in the Active Directory.

Designer name: **Rename object**. Official reference: [Active Directory / Rename object](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#renameobject).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |
| New name | Required | Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Object already exists`, `Active Directory error`.

---

### Create user

Creates a user in the Active Directory.

Designer name: **Create user**. Official reference: [Active Directory / Create user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#createuser).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Location | Optional | Text value | — |
| First name | Required | Text value | — |
| Initials | Optional | Text value | — |
| Last name | Optional | Text value | — |
| Username | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Password never expires | Choice | Boolean value | False |
| Disabled account | Choice | Boolean value | False |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object already exists`, `Couldn't set or update password`, `Active Directory error`.

---

### Get user info

Reads a user's information in the Active Directory.

Designer name: **Get user info**. Official reference: [Active Directory / Get user info](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#getuserinfo).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |

**Outputs**

| Variable | Type |
|---|---|
| UserInfo | User info |

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Active Directory error`.

---

### Modify user

Modify a user in the Active Directory.

Designer name: **Modify user**. Official reference: [Active Directory / Modify user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#modifyuseraction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |
| Operation | Choice | Enable/disable user, Rename user, Delete user, Reset password | Enable/disable user |
| Enable user | Choice | Boolean value | False |
| New name | Required | Text value | — |
| New password | Required | Direct encrypted input or Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Object already exists`, `Invalid attribute syntax`, `Active Directory error`, `Couldn't set or update password`.

---

### Unlock user

Unlocks an Active Directory user.

Designer name: **Unlock user**. Official reference: [Active Directory / Unlock user](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#unlockuser).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Active Directory error`.

---

### Update user info

Updates a user's information in the Active Directory.

Designer name: **Update user info**. Official reference: [Active Directory / Update user info](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#updateuserinfo).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |
| Distinguished name | Required | Text value | — |
| Display name | Optional | Text value | — |
| First name | Optional | Text value | — |
| Initials | Optional | Text value | — |
| Last name | Optional | Text value | — |
| Title | Optional | Text value | — |
| The email of the user | Optional | Text value | — |
| The company of the user | Optional | Text value | — |
| Telephone number | Optional | Text value | — |
| Extension | Optional | Text value | — |
| City | Optional | Text value | — |
| Postal code | Optional | Text value | — |
| State | Optional | Text value | — |
| Country | Choice | Afghanistan, Åland Islands, Albania, Algeria, American Samoa, Andorra, Angola, Anguilla, Antarctica, Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bermuda, Bhutan, State of Bolivia Plurinational, Bonaire, Bosnia and Herzegovina, Botswana, Bouvet Island, Brazil, British Indian Ocean Territory, Brunei Darussalam, Bulgaria, Burkina Faso, Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Cayman Islands, Central African Republic, Chad, Chile, China, Christmas Island, Cocos (Keeling) Islands, Colombia, Comoros, Congo, Democratic Republic of the Congo, Cook Islands, Costa Rica, Côte d'Ivoire, Croatia, Cuba, Curaçao, Cyprus, Czech Republic, Denmark, Djibouti, Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Ethiopia, Falkland Islands, Faroe Islands, Fiji, Finland, France, French Guiana, French Polynesia, French Southern Territories, Gabon, Gambia, Georgia, Germany, Ghana, Gibraltar, Greece, Greenland, Grenada, Guadeloupe, Guam, Guatemala, Guernsey, Guinea, Guinea-Bissau, Guyana, Haiti, Heard Island and McDonald Islands, Holy See, Honduras, Hong Kong Special Administrative Region, Hungary, Iceland, India, Indonesia, Islamic Republic of Iran, Iraq, Ireland, Isle of Man, Israel, Italy, Jamaica, Japan, Jersey, Jordan, Kazakhstan, Kenya, Kiribati, Democratic Peoples Republic of Korea, Republic of Korea, Kuwait, Kyrgyzstan, Lao People's Democratic Republic, Latvia, Lebanon, Lesotho, Liberia, Libya, Liechtenstein, Lithuania, Luxembourg, Macao Special Administrative Region, North Macedonia, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Martinique, Mauritania, Mauritius, Mayotte, Mexico, Micronesia, Moldova, Monaco, Mongolia, Montenegro, Montserrat, Morocco, Mozambique, Myanmar, Namibia, Nauru, Nepal, Netherlands, New Caledonia, New Zealand, Nicaragua, Niger, Nigeria, Niue, Norfolk Island, Northern Mariana Islands, Norway, Oman, Pakistan, Palau, Palestinian Authority, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Pitcairn, Poland, Portugal, Puerto Rico, Qatar, Réunion, Romania, Russia, Rwanda, Saint Barthélemy, Saint Helena, Ascension, Tristan da Cunha, Saint Kitts and Nevis, Saint Lucia, Saint Martin (French part), Saint Pierre and Miquelon, Saint Vincent and the Grenadines, Samoa, San Marino, São Tomé and Príncipe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Sint Maarten (Dutch part), Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, South Georgia and the South Sandwich Islands, South Sudan, Spain, Sri Lanka, Sudan, Suriname, Svalbard and Jan Mayen, Swaziland, Sweden, Switzerland, Syrian Arab Republic, Taiwan, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Tokelau, Tonga, Trinidad and Tobago, Tunisia, Türkiye, Turkmenistan, Turks and Caicos Islands, Tuvalu, Uganda, Ukraine, United Arab Emirates, United Kingdom of Great Britain and Northern Ireland, United States of America, United States Minor Outlying Islands, Uruguay, Uzbekistan, Vanuatu, Bolivarian Republic of Venezuela, Vietnam, Virgin Islands (British), Virgin Islands (U.S.), Wallis and Futuna, Yemen, Zambia, Zimbabwe, None | None |

Produces no variables.

**On error:** `Authentication error`, `Invalid operation`, `The server isn't operational`, `Unauthorized access`, `Active Directory entry not found`, `Object doesn't exist on server`, `Couldn't set or update password`, `Active Directory error`.

---

### Connect to server

Connects to an Active Directory server.

Designer name: **Connect to server**. Official reference: [Active Directory / Connect to server](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#connecttoserveraction).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| LDAP path | Required | Text value | — |
| Use authentication | Choice | Boolean value | False |
| Username | Required | Text value | — |
| Password | Required | Direct encrypted input or Text value | — |
| Authentication type | Choice | None, Secure, Encryption, Secure sockets layer, Read-only server, Anonymous, Fast bind, Signing, Sealing, Delegation, Server bind | Secure |

**Outputs**

| Variable | Type |
|---|---|
| ParentDirectoryEntry | Active Directory entry |

**On error:** `Authentication error`, `Unauthorized access`, `The server isn't operational`, `Invalid operation`, `Active Directory error`.

---

### Close connection

Closes the connection with the Active Directory server.

Designer name: **Close connection**. Official reference: [Active Directory / Close connection](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/activedirectory#closeconnection).

**Inputs**

| Parameter | Required | Accepts | Default |
|---|---|---|---|
| Parent directory entry | Required | Active Directory entry | — |

Produces no variables.

No module-specific exceptions are listed for this action.

---
