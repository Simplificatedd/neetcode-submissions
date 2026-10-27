class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = set()

        for email in emails:
            local_name, domain_name = email.split("@")

            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")

            uniqueEmail.add(local_name + "@" + domain_name)

        return len(uniqueEmail)