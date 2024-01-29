#!/usr/bin/env python3
""" Test client """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient Return"""
        endpoint = f'https://api.github.com/orgs/{org_name}'
        github_org_client = GithubOrgClient(org_name)
        github_org_client.org()
        mock_get_json.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        mock_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}
        org_name = "google"

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload
            github_org_client = GithubOrgClient(org_name)
            self.assertEqual(github_org_client._public_repos_url,
                             mock_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """test GithubOrgClient.public_repos"""
        mock_payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = mock_payload
        mock_repos_url = "https://api.github.com/orgs/test/repos"

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:
            mocked_public.return_value = mock_repos_url
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])
            mocked_public.assert_called_once()
            mocked_method.assert_called_once_with(mock_repos_url)


if __name__ == "__main__":
    unittest.main()
